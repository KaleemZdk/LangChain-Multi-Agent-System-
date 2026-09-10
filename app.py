import streamlit as st
from src.pipelines.pipeline import research_pipeline
from src.agents.agents import build_search_agent, build_reader_agent,writer_chain,critic_chain

st.set_page_config(page_title="AI Research Assistant", page_icon="🔍")

st.title("🔍 Ai Research Assistant")
st.write("Enter a topic and let the multi-agent system research, write, and critique a report.")

topic = st.text_input("Research Topic", placeholder="e.g. Latest trends in renewable energy")

if st.button("Run Research Pipeline", type="primary"):
    if not topic.strip():
        st.warning("Please enter a topic first.")
    else:
        with st.spinner("Step 1: Searching..."):
            pass  # actual progress shown via pipeline's print statements in terminal

        try:
            result = research_pipeline(topic)

            st.success("Pipeline complete!")

            st.subheader("📄 Final Report")
            st.markdown(result["report"])

            with st.expander("🔎 Search Results"):
                st.write(result["search_results"])

            with st.expander("📚 Scraped Content"):
                st.write(result["scraped_content"])

            with st.expander("🧐 Critic Feedback"):
                st.markdown(result["feedback"])

        except Exception as e:
            st.error(f"Something went wrong: {e}")




def research_pipeline(topic:str)-> dict:

    state={

    }

    print("\n"+"="*50)
    print("step 1 - serach agent is working ...")
    print("="*50)

    search_agent = build_search_agent()
    search_result = search_agent.invoke({
        "messages": [("user", f"find recent, reliable and detailed information about: {topic}")]
    })

    state["search_results"] = search_result['messages'][-1].content
    print("\n search result", state['search_results'])

    #step 2 - reader agent
    print("\n"+ "="*50)
    print("step 2 - Reader agent is scraping top resources ...")
    print("="*50)

    reader_agent = build_reader_agent()
    reader_result = reader_agent.invoke({
        "messages": [("user",
            f"Based on the following search results about '{topic}', "
            f"pick the most relevant URL and scrape it for deeper content.\n\n"
            f"Search Results:\n{state['search_results'][:800]}"
        )]
    })

    state['scraped_content'] = reader_result['messages'][-1].content

    print("\nscraped content: \n", state['scraped_content'])


     #step 3 - writer chain
    print("\n"+ "="*50)
    print("step 3 - Writer is drafting the report ...")
    print("="*50)

    research_combined = (
        f"SEARCH RESULTS : \n {state['search_results']} \n\n"
        f"DETAILED SCRAPED CONTENT : \n {state['scraped_content']}"
    )

    state["report"] = writer_chain.invoke({
        "topic" : topic,
        "research" : research_combined
    })

    print("\n Final Report\n",state['report'])

    #critic report 
    print("\n"+ "="*50)
    print("step 4 - Critic is reviewing ther report")
    print("="*50)

    state["feedback"] = critic_chain.invoke({
        "report": state['report']
    })

    print("\n Critic Report\n",state['feedback'])  
    return state