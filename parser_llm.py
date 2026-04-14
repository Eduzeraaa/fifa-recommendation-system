import os
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()


class Saida_esperada(BaseModel):
    orcamento: int = Field(description='Orçamento do usuário, em milhões de Euros (se o usuário disser 50 milhões, o valor aqui deve ser 50.000.000).')
    posicao: str = Field(description='''Extraia a posição do jogador mencionada pelo usuário.

Responda apenas com uma das opções abaixo:
- goleiro
- zagueiro
- lateral direito
- lateral esquerdo
- volante
- meia
- ponta direita
- ponta esquerda
- atacante

Regras:
- Retorne somente uma palavra ou expressão da lista acima
- Não explique nada
- Não invente novas posições
- Se não houver posição clara, retorne "desconhecido"''')
    

model = ChatGroq(
    api_key=os.environ.get('GROQ_API_KEY'),
    model_name='llama-3.1-8b-instant'
)

llm_estruturada = model.with_structured_output(Saida_esperada)

def parser(pergunta):
    return llm_estruturada.invoke(pergunta)
