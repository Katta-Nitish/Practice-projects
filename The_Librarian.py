import chromadb
import requests
import sys
sys.stdout.reconfigure(encoding='utf-8')
n=0
url="https://www.gutenberg.org/files/1661/1661-0.txt"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response=requests.get(url,headers=headers).text
response=response.replace("\r\n", " ")
chunks=[]
for i in range(0,len(response),1000):
  chunks.append(response[i:i+1000])
  n+=1
cli=chromadb.Client()
Collection=cli.get_or_create_collection(name="Sherlock_Holmes")
Collection.add(
  documents=chunks,
  ids=[str(x) for x in range(1,n+1)]
)
result=Collection.query(query_texts=["The detectives apartment in London"],
                        n_results=2)
print(str(result))

