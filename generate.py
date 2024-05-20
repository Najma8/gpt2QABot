from question import ask_question
from transformers import AutoTokenizer, GPT2LMHeadModel, GPT2Tokenizer

def getModelTokenizer(lang):
    if lang.lower()=='en':
        tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        model = GPT2LMHeadModel.from_pretrained("./model_en")
    elif lang.lower()=='tr':
        tokenizer = AutoTokenizer.from_pretrained("ytu-ce-cosmos/turkish-gpt2")
        model = GPT2LMHeadModel.from_pretrained("./model_tr")
    return model, tokenizer

if __name__ == '__main__':
    chain =""
    lang = input("Language (en/tr): ")
    model, tokenizer = getModelTokenizer(lang)
    while True:
        user_input = input("\nQuestion: ")
        if user_input.lower() == 'end':
            print("Kapaniyor")
            break
        else:
            chain = chain+"[Q] "+user_input+"\n"
            answer = ask_question(chain, max_new_tokens=200, temperature=0.8, top_k=50, top_p=0.95, model=model, tokenizer=tokenizer)
            #print("\nQuestion: ", user_input)
            chain = chain+"[A] "+answer+"\n"
            print("\nAnswer: ", answer)
