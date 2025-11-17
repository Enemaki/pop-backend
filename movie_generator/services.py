# from langchain_text_splitters import RecursiveCharacterTextSplitter
# import os

# from dotenv import load_dotenv
# from google import genai
# from supabase import create_client, Client
# load_dotenv()

# url: str = os.environ.get("SUPABASE_URL")
# key: str = os.environ.get("SUPABASE_KEY")
# supabase: Client = create_client(url, key)

# def embedding(text_list):
#     client = genai.Client(api_key=os.environ.get("MOVIES_EMBED_API_KEY"))
#     movie_data = []

#     for text in text_list:
#         result = client.models.embed_content(
#                 model="text-embedding-004",
#                 contents=text)
#         embedding_vector = result.embeddings[0].values
#         movie_data.append({ "content": text, "embedding": embedding_vector })
    
#     supabase.table("popchoice").insert(movie_data).execute()
#     print("Data inserted successfully")
    

# with open('C:/Users/musty/OneDrive/Desktop/tech projects/Popchoice/pop-backend/movie_generator/movies.txt') as f:
#     movie_info = f.read()

# text_splitter = RecursiveCharacterTextSplitter(
#     # Set a really small chunk size, just to show.
#     chunk_size=250,
#     chunk_overlap=35,
# )

# texts = text_splitter.create_documents([movie_info])
# movie_list = []
# for text in texts:
#     movie_list.append(text.page_content)
# print(movie_list)
# embedding(movie_list)



# # users_email = "mustyeneye@gmail.com"
# # users_password = "Vb$JLrGL9&WX&DM"

# # supabase.auth.sign_in_with_password({ "email": users_email, "password": users_password })
# # print(user)

# # response = supabase.table("documents").select("*").execute()
# # print(response.data)

# # supabase.table("documents").insert({}).execute()