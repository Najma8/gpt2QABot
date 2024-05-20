#response generation for [Q]/[A] format
import torch

def ask_question(input_question, max_new_tokens, temperature, top_k, top_p, model, tokenizer):
    model.eval()
    with torch.no_grad():
        input_text = input_question
        print(input_text)
        encoded_input = tokenizer.encode_plus(
            input_text,
            add_special_tokens=True,
            return_tensors='pt',
            truncation=True
        )
        output = model.generate(
            input_ids=encoded_input['input_ids'],
            attention_mask=encoded_input['attention_mask'],
            max_new_tokens=max_new_tokens,
            do_sample=True,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
            num_return_sequences=1
        )
        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
        answer_part = generated_text[len(input_text):]
        start_index = answer_part.find('[A]')
        end_index = answer_part.find('[Q]')
        if start_index != -1 and end_index != -1:
            answer = answer_part[(start_index + 3):end_index]
        else:
            answer = "Markers not found or incomplete."
        return answer.strip()
