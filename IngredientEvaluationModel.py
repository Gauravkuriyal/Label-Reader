import os
import google.generativeai as genai

genai.configure(api_key="__Your_API_Key")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "INGREDIENTS:REFINEDWHEATFLOUR(MAIDA)(70%),SUGAR,REFINED PALMOIL,EDIBLESTARCHESS(MAIZE-2.7%&ARROWR00T-0.1%),MILK SOLIDS,RAISINGAGENTS[503(i)8500(i)},{INVERTSUGARSYRUP, IDISEDSALT,EMULSIFIERS(322&472e),DOUGHCONDITIONER(223) ANDIMPROVER[1101(i)] CONTAINSPERMITTEDNATURALF0ODC0LOUR(150d)ANDADDED FLAVOURS(ARTIFICIALFLAVOURINGSUBSTANCES-BUTTERSCOTCH) (NumbersinbracketsasperInternationalNumberingSystem) CONTAINSWHEAT,MILK,SOYAANDSULPHITE.\n\nGive me the brief description of each and every ingredient. Also tell me which are harmful or unhealthy and tolerable amount for them too. Also tell me whether they are in tollerable amount in given description or not.\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "This ingredient list is for a baked good, likely a type of cookie or biscuit. Let's break down each ingredient, its potential health impacts, and whether its presence in the list suggests a concerning amount.  Note: Determining \"tolerable amounts\" requires knowing the serving size, which isn't provided.  The following analysis focuses on the ingredients themselves and their general health implications.\n\n**Ingredients and Analysis:**\n\n* **Refined Wheat Flour (Maida) (70%):** This is highly refined white flour, lacking much fiber and nutrients.  It's a primary source of simple carbohydrates, leading to rapid blood sugar spikes.  **Unhealthy in excess.**  70% indicates a very high proportion, likely contributing significantly to the product's overall calorie and simple carbohydrate content.  **Not tolerable in this high proportion without careful portion control.**\n\n* **Sugar:**  Added sugar contributes empty calories and is linked to weight gain, type 2 diabetes, heart disease, and other health problems.  **Unhealthy in excess.** The exact amount isn't specified, but its presence is a major concern.  **Not tolerable without knowing the exact quantity and considering individual health needs.**\n\n* **Refined Palm Oil:**  A source of saturated fat, which can raise LDL (\"bad\") cholesterol levels and increase heart disease risk.  **Unhealthy in excess.**  The amount is unspecified, raising potential concerns.  **Not tolerable without knowing the quantity.**\n\n* **Edible Starches (Maize - 2.7% & Arrowroot - 0.1%):** These are relatively neutral; maize starch (cornstarch) is a common food additive. Arrowroot is a less processed starch.  These are generally considered safe in moderate amounts.  The percentages are low, suggesting minimal impact on health. **Tolerable in these small quantities.**\n\n* **Milk Solids:**  Provides protein and some calcium.  Can be a problem for people with lactose intolerance. **Generally considered healthy, but can be a problem for some.** Amount unspecified, impact unclear.\n\n* **Raising Agents (503(i) & 8500(i)):** These are baking powders/soda.  503(i) is ammonium bicarbonate, and 8500(i) is disodium diphosphate.  Generally considered safe in baking amounts.  **Tolerable.**\n\n* **Invert Sugar Syrup:** A mixture of glucose and fructose, leading to a similar blood sugar response as sucrose (table sugar).  **Unhealthy in excess.** Amount unspecified. **Not tolerable without knowing the quantity.**\n\n* **Iodised Salt:**  Provides iodine, an essential nutrient, but excessive sodium intake is linked to hypertension.  **Unhealthy in excess.**  Amount unspecified. **Not tolerable without knowing the quantity.**\n\n* **Emulsifiers (322 & 472e):**  322 is lecithin (often from soy), and 472e is mono- and diglycerides of fatty acids.  Generally considered safe, but some individuals might experience digestive issues.  **Generally tolerable, but individual sensitivities vary.**\n\n* **Dough Conditioner (223):** This is likely calcium phosphate, acting as a dough strengthener. Generally considered safe.  **Tolerable.**\n\n* **Improver (1101(i)):** This is likely riboflavin (Vitamin B2), which aids baking process but is found naturally in food as well.  **Generally tolerable.**\n\n* **Permitted Natural Food Colour (150d):**  This is a caramel colour.  Generally considered safe, but some studies suggest potential issues with high consumption.  **Tolerable in small amounts.**\n\n* **Added Flavours (Artificial Flavouring Substance - Butterscotch):**  Artificial flavorings are generally considered safe but might contain potentially harmful chemicals, and their long-term health effects are not fully understood.  **Potentially concerning, especially with regular consumption.**  Amount not specified, impact unclear.\n\n* **Contains Wheat, Milk, Soya, and Sulphite:** This indicates potential allergens. Important for individuals with allergies or sensitivities.\n\n\n**Overall:**\n\nThis food product contains a high proportion of refined carbohydrates, added sugar, and saturated fat, making it potentially unhealthy if consumed regularly in large quantities.  The lack of specific amounts for many ingredients makes a complete health assessment impossible.  To determine tolerability, you'd need to know serving size, nutritional information per serving, and the individual's health status and dietary needs.  It is advisable to consume this product in moderation, if at all, if concerned about your health.\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "INGREDIENTS:REFINEDWHEATFLOUR(MAIDA)(70%),SUGAR,REFINED PALMOIL,EDIBLESTARCHESS(MAIZE-2.7%&ARROWR00T-0.1%),MILK SOLIDS,RAISINGAGENTS[503(i)8500(i)},{INVERTSUGARSYRUP, IDISEDSALT,EMULSIFIERS(322&472e),DOUGHCONDITIONER(223) ANDIMPROVER[1101(i)] CONTAINSPERMITTEDNATURALF0ODC0LOUR(150d)ANDADDED FLAVOURS(ARTIFICIALFLAVOURINGSUBSTANCES-BUTTERSCOTCH) (NumbersinbracketsasperInternationalNumberingSystem) CONTAINSWHEAT,MILK,SOYAANDSULPHITE.\n\nGive me the brief description of each and every ingredient. Also tell me which are harmful or unhealthy and tolerable amount for them too. Also tell me whether they are in tollerable amount in given description or not.",
        "INGREDIENTS:REFINEDWHEATFLOUR(MAIDA)(70%),SUGAR,REFINED PALMOIL,EDIBLESTARCHESS(MAIZE-2.7%&ARROWR00T-0.1%),MILK SOLIDS,RAISINGAGENTS[503(i)8500(i)},{INVERTSUGARSYRUP, IDISEDSALT,EMULSIFIERS(322&472e),DOUGHCONDITIONER(223) ANDIMPROVER[1101(i)] CONTAINSPERMITTEDNATURALF0ODC0LOUR(150d)ANDADDED FLAVOURS(ARTIFICIALFLAVOURINGSUBSTANCES-BUTTERSCOTCH) (NumbersinbracketsasperInternationalNumberingSystem) CONTAINSWHEAT,MILK,SOYAANDSULPHITE.\n\nGive me the brief description of each and every ingredient. Also tell me which are harmful or unhealthy and tolerable amount for them too. Also tell me whether they are in tollerable amount in given description or not.\n\nprovide the response in json like:",
        "{ingredients: [{\nname:\"Ingredient1\",\ndescription:\"response for the ingredient\"\n},\n{\nname:\"Ingredient2\",\ndescription:\"response for the ingredient\"\n},\n],\nconclusion:\"concluded response...\"\n}\n\nyou can modify this response as you like and provide more information. \n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\n  \"ingredients\": [\n    {\n      \"name\": \"Refined Wheat Flour (Maida) (70%)\",\n      \"description\": \"Highly refined white flour, lacking fiber and nutrients.  Provides simple carbohydrates leading to rapid blood sugar spikes. Unhealthy in excess. 70% is a very high proportion, likely making this product high in calories and simple carbs.  Not tolerable in this high proportion for most individuals without careful portion control.\",\n      \"health_impact\": \"Unhealthy in excess\",\n      \"tolerable_amount\": \"Individualized; depends on overall diet and health goals.  This amount is likely too high for many.\"\n    },\n    {\n      \"name\": \"Sugar\",\n      \"description\": \"Added sugar contributes empty calories and is linked to weight gain, type 2 diabetes, heart disease, and other health problems. Unhealthy in excess. Amount unspecified, therefore impact unclear.\",\n      \"health_impact\": \"Unhealthy in excess\",\n      \"tolerable_amount\": \"Individualized;  American Heart Association recommends no more than 25 grams added sugar per day for women and 36 grams for men.  The amount in this product is unknown and potentially concerning.\"\n    },\n    {\n      \"name\": \"Refined Palm Oil\",\n      \"description\": \"A source of saturated fat, which can raise LDL cholesterol and increase heart disease risk. Unhealthy in excess. Amount unspecified, raising potential concerns.\",\n      \"health_impact\": \"Unhealthy in excess\",\n      \"tolerable_amount\": \"Individualized; depends on overall fat intake.  Amount in this product is unknown and could be problematic.\"\n    },\n    {\n      \"name\": \"Edible Starches (Maize - 2.7% & Arrowroot - 0.1%)\",\n      \"description\": \"Relatively neutral; cornstarch (maize) is common, and arrowroot is a less processed starch. Generally considered safe in moderate amounts.  Percentages are low, suggesting minimal health impact.\",\n      \"health_impact\": \"Generally safe\",\n      \"tolerable_amount\": \"The amounts present are likely tolerable for most individuals.\"\n    },\n    {\n      \"name\": \"Milk Solids\",\n      \"description\": \"Provides protein and some calcium. Can be a problem for people with lactose intolerance. Amount unspecified, impact unclear.\",\n      \"health_impact\": \"Generally healthy, but may cause issues for those with lactose intolerance.\",\n      \"tolerable_amount\": \"Amount unknown; depends on individual tolerance to lactose.\"\n    },\n    {\n      \"name\": \"Raising Agents [503(i) & 8500(i)] (Ammonium Bicarbonate & Disodium Diphosphate)\",\n      \"description\": \"Baking powders/soda. Generally considered safe in baking amounts.\",\n      \"health_impact\": \"Generally safe\",\n      \"tolerable_amount\": \"Amounts used in baking are typically safe.\"\n    },\n    {\n      \"name\": \"Invert Sugar Syrup\",\n      \"description\": \"A mixture of glucose and fructose, leading to a similar blood sugar response as sucrose. Unhealthy in excess. Amount unspecified.\",\n      \"health_impact\": \"Unhealthy in excess\",\n      \"tolerable_amount\": \"Amount unknown; should be consumed in moderation.\"\n    },\n    {\n      \"name\": \"Iodised Salt\",\n      \"description\": \"Provides iodine, but excessive sodium is linked to hypertension. Unhealthy in excess. Amount unspecified.\",\n      \"health_impact\": \"Unhealthy in excess\",\n      \"tolerable_amount\": \"Amount unknown;  limit sodium intake for heart health.\"\n    },\n    {\n      \"name\": \"Emulsifiers (322 & 472e) (Lecithin & Mono- and Diglycerides of Fatty Acids)\",\n      \"description\": \"Generally considered safe, but some individuals might experience digestive issues.\",\n      \"health_impact\": \"Generally safe, but individual sensitivities vary.\",\n      \"tolerable_amount\": \"Amounts typically used in food are generally safe.\"\n    },\n    {\n      \"name\": \"Dough Conditioner (223) (Likely Calcium Phosphate)\",\n      \"description\": \"Generally considered safe.\",\n      \"health_impact\": \"Generally safe\",\n      \"tolerable_amount\": \"Amount used in baking is typically safe.\"\n    },\n    {\n      \"name\": \"Improver [1101(i)] (Likely Riboflavin)\",\n      \"description\": \"Likely riboflavin (Vitamin B2). Generally tolerable.\",\n      \"health_impact\": \"Generally safe\",\n      \"tolerable_amount\": \"Amounts used are typically safe.\"\n    },\n    {\n      \"name\": \"Permitted Natural Food Colour (150d) (Caramel Colour)\",\n      \"description\": \"Generally considered safe, but potential issues with high consumption.\",\n      \"health_impact\": \"Generally safe in small amounts\",\n      \"tolerable_amount\": \"Amount unknown;  consume in moderation.\"\n    },\n    {\n      \"name\": \"Added Flavours (Artificial Flavouring Substance - Butterscotch)\",\n      \"description\": \"Artificial flavorings; potential harmful chemicals; long-term health effects not fully understood. Amount not specified.\",\n      \"health_impact\": \"Potentially concerning with regular consumption\",\n      \"tolerable_amount\": \"Amount unknown;  limit consumption of artificial flavors.\"\n    },\n    {\n      \"name\": \"Contains Wheat, Milk, Soya, and Sulphite\",\n      \"description\": \"Indicates potential allergens.\",\n      \"health_impact\": \"Allergenic for some individuals\",\n      \"tolerable_amount\": \"Avoid if allergic.\"\n    }\n  ],\n  \"conclusion\": \"This product contains a high proportion of refined carbohydrates, added sugar, and saturated fat, making it potentially unhealthy if consumed regularly in large quantities.  The lack of specific amounts for many ingredients makes a complete health assessment impossible.  To determine tolerability, you need to know serving size and nutritional information per serving, and consider individual health status and dietary needs.  It is advisable to consume this product sparingly or not at all if health is a concern.  Individuals with allergies or sensitivities to wheat, milk, soy, or sulfites should avoid this product.\"\n}\n```\n",
      ],
    },
  ]
)

def GenerateResponse(ingredients):
    string = ingredients+'''\n
        Give me the description of each and every ingredient. Also tell me which are harmful or unhealthy and tolerable amount for them too. Also try to tell the names of complex ingredient in simple terms like specify the corn syrup as sugar in the description. Also tell me whether they are in tollerable amount in given description or not.",
        \nprovide the response in json like:",
        "{ingredients: [{\nname:\"Ingredient1\",\ndescription:\"response for the ingredient\"\n,\n      \"health_impact\": \"response\",\n      \"tolerable_amount\": \"response\"\n},\n{\nname:\"Ingredient2\",\ndescription:\"response for the ingredient\"\n,\n      \"health_impact\": \"response\",\n      \"tolerable_amount\": \"response\"\n},\n],\nconclusion:\"concluded response...\"\n}
    '''
    response = chat_session.send_message(string)

    # print(response.text)
    return response.text