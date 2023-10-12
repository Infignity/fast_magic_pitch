from langchain.prompts import PromptTemplate


prompt_temps = PromptTemplate(
    input_variables=['company_data', 'product_services', 'solution', 'pricing'],
    template="Dear AI, as a seasoned B2B marketer with sophisticated analytical capabilities, I require your assistance in processing a set of unstructured data from our company website. The goal is to convert this raw data into comprehensive, actionable marketing strategy variables. In doing so, please consider the following data segments:\n\n"
    "[Input- HomePage: {company_data}], [Input- Products/Services Page: {product_services}], [Input- Solutions Page: {solution}], [Input- Pricing Page: {pricing}].\n\n"
    "Output:\n\n"
    "[Input: Company Description]: From the HomePage content, distill a detailed account of our company's mission, history, key services, target market, and unique strengths. Additionally, outline any competitive advantages and key accomplishments that distinguish us in the market.\n\n"
    "For each product/service from the Products/Services Page:\n"
    "[Input: Product/Service Name and Detailed Description]: Identify the name of each product or service and provide an in-depth description. This description should cover the conceptual basis of the product/service, the technology involved, its intended purpose, and the problems it solves.\n\n"
    "[Input: Comprehensive Product/Service Features]: Identify and describe the main features, functions, uses, benefits, and specifications of each product or service. Discuss any innovative aspects or proprietary technology involved, and highlight how these features contribute to the overall value proposition.\n\n"
    "[Input: Unique Selling Proposition (USP)]: Analyze and articulate what distinguishes each of our product/service from its competition. Identify the overarching USP of the company as a whole, as well as the unique USPs for each individual product/service. Discuss any patents, first-to-market advantages, superior design or technology, customer service excellence, or any other differentiators.\n\n"
    "[Input: Service Usage Scenarios]: Using the information from the Solutions Page, elaborate on potential use-cases for each product or service. Provide comprehensive examples showcasing how our products/services could be used by clients in a variety of situations or industries, emphasizing their value and versatility.\n\n"
    "[Input: Solutions offered by each Product/Service]: Unpack the solutions offered by each product/service in depth. Describe how each solution addresses a customer's specific pain points or challenges, and how it contributes to their success.\n\n"
    "[Input: All Pricing Tiers]: From the Pricing Page, deliver thorough descriptions of our different pricing tiers or packages for each product/service. This should include specifics on what each tier includes, the exact pricing, any discounts for bulk or long-term purchases, and who it's ideally suited for. Ensure that every detail provided on the Pricing Page is covered and communicated effectively.\n\n"
    "[Input: Ideal Customer Profile (ICP)]: Identify our ideal customer profile based on the services we offer, our mission, and our target market. Consider their industry, company size, job title, pain points, goals, and any other pertinent information.\n\n"
    "[Input: Buyer Persona]: Develop buyer personas based on the behavior patterns, motivations, and goals of our different customer segments. Describe their demographics, behavioral traits, motivations, and buying patterns. Use this information to understand and describe how our products or services could meet their specific needs.\n\n"
    "[Input: Market Position]: Analyze our current position in the market relative to our competitors. Consider factors like market share, brand recognition, reputation, and customer perceptions. Discuss how our products or services, pricing strategies, and overall value proposition contribute to this market position.\n\n"
    "[Input: Competitor Analysis]: Perform a thorough competitor analysis. Identify our key competitors and analyze their products/services, pricing strategies, USPs, strengths, and weaknesses. Use this analysis to identify opportunities and threats, as well as areas where our company can differentiate itself."
)