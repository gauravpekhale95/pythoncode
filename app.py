# fast api server 

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)   

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI server!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000, log_level="info")


# write a python code to invoke chat gpt chat completion using openai module by taking below input 
#  1 - text file (directly pass the text file do not read and pass the content )
#  2 - image file (directly pass the image file do not read and pass the content )
# 3 - prompt (string) : Use instructions in text file and perform as per instrcttions
# import openai
# #  set open ai key 


# def invoke_chatgpt_with_files(text_file, image_file, prompt):
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-4",
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": prompt}
#             ],
#             files=[
#                 {"file": text_file, "purpose": "instruction"},
#                 {"file": image_file, "purpose": "image"}
#             ]
#         )
#         return response.choices[0].message['content']
#     except Exception as e:
#         return str(e) 
    
# # Example usage:

# response = invoke_chatgpt_with_files(
#     text_file="1.txt",
#     image_file="img1.png",
#     prompt="Use the instructions in the text file and perform as per instructions."
# )
# print(response)