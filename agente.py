# agente.py
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

FERRAMENTAS = {
    "calcular": lambda expr: str(eval(expr)),  # só para demo — substitua por algo seguro
    }

    messages = [{"role": "system", "content":
        "Você é um agente. Quando precisar calcular, responda apenas com: CALCULAR:<expressão>"}]

        while True:
            pergunta = input("Você: ")
                messages.append({"role": "user", "content": pergunta})

                    while True:
                            resp = client.chat.completions.create(
                                        model="gpt-4o-mini", messages=messages)
                                                msg = resp.choices[0].message.content
                                                        if msg.startswith("CALCULAR:"):
                                                                    resultado = FERRAMENTAS["calcular"](msg.split(":")[1])
                                                                                messages.append({"role": "user", "content": f"Resultado: {resultado}"})
                                                                                        else:
                                                                                                    print("Agente:", msg)
                                                                                                                messages.append({"role": "assistant", "content": msg})
                                                                                                                            break