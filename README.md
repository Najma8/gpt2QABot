# Custom Question-Answering ChatBot


This project implements an interactive web application for a chatbot capable of answering user questions in English and Turkish, specifically tailored for the custom data of OSTIM Technical University. The chatbot utilizes fine-tuned GPT-2 language models for each language to generate responses to user inquiries.
> This project doesn't include the fine-tuning process/codes yet and only includes the fine-tuned models, the response generation steps and the streamlit interface!

## Features

- **Language Selection**: Users can choose between English and Turkish languages for their questions.
- **Real-Time Interaction**: Interactive web interface powered by Streamlit allows seamless communication with the chatbot.
- **Question-Answering**: The chatbot generates responses based on the input questions using pre-trained GPT-2 language models.
- **Conversation History**: Maintains a history of user inputs and bot replies for reference during the conversation.

## Training Dataset and Model Details
The chatbot models were fine-tuned on custom datasets specifically in Question-Answer format to better understand and generate relevant responses for given context.

####English Model
Model: Fine-tuned OpenAI GPT-2
Dataset: The English model was trained on a dataset comprising academic questions and answers, specific to the subjects and areas of expertise at OSTIM Technical University.
Training Process: The fine-tuning process involved supervised learning where the pre-trained GPT-2 model was further trained on the curated dataset and many different configurations to improve its contextual understanding and response accuracy.
####Turkish Model
Model: Fine-tuned ytu-ce-cosmos Turkish GPT-2
Dataset: The Turkish model was trained on a dataset containing similar academic questions and answers but translated and adapted to Turkish language contexts. The complex layers and weights of the turkish model had its effect on response accuracy and contextual understanding!
Training Process: Similar to the English model, the Turkish model was fine-tuned using supervised learning techniques and different configurations to fit best the model's weights and complex layers to enhance its performance in generating contextually appropriate responses in Turkish.

## Files Overview

- **`QAapp.py`**: Main Python file containing the Streamlit application code for the chatbot interface.
- **`question.py`**: Python file defining functions for question-answering using the language models.
- **`generate.py`**: Python file providing functions to load the appropriate tokenizer and language model based on the selected language.
- **`htmlTemplates.py`**: Python file containing HTML templates for formatting chatbot messages.
- **`model_en`**: Fine-tuned OpenAI/gpt2 model for English language question-answering.
- **`model_tr`**: Fine-tuned ytu-ce-cosmos/turkish-gpt2 model for Turkish language question-answering.
- **`requirements.txt`**: Includes the primary libraries and their versions required for the project.

--------------------------

# Özel Soru-Cevap ChatBotu


Bu proje, OSTİM Teknik Üniversitesi'nin özel verilerine göre özel olarak tasarlanmış, kullanıcı sorularını İngilizce ve Türkçe olarak yanıtlayabilen bir chatbot için etkileşimli bir web uygulaması gerçekleştirmektedir. Chatbot, kullanıcı sorularına yanıtlar oluşturmak için her dil için ince ayarlı(fine-tuned) GPT-2 dil modellerini kullanıyor.
> Bu proje henüz ayarlama işlemini (fine-tuning adımlarını)/kodlarını içermez, yalnızca ayarlanmış modelleri, cevap üretim adımlarını ve Streamlit arayüzünü içerir!

## Özellikler

- **Dil Seçimi**: Kullanıcılar soruları için İngilizce ve Türkçe dilleri arasından seçim yapabilirler.
- **Gerçek Zamanlı Etkileşim**: Streamlit tarafından desteklenen etkileşimli web arayüzü, sohbet robotu ile sorunsuz iletişime olanak tanır.
- **Soru-Cevap**: Sohbet robotu, önceden eğitilmiş GPT-2 dil modellerini kullanarak girdi sorularına yanıtlar üretir.
- **Sohbet Geçmişi**: Konuşma sırasında referans için kullanıcı girdilerinin ve bot yanıtlarının bir geçmişini korur.

## Eğitim Veri Seti ve Model Detayları
Sohbet robotu modelleri, verilen bağlam için ilgili yanıtlar üretebilmek için Soru-Cevap formatında özelleştirilmiş veri setleri üzerinde ayarlandı.

####İngilizce Model
Model: Ayarlanmış OpenAI/gpt2
Veri Seti: İngilizce model, OSTİM Teknik Üniversitesi'nin konularına ve uzmanlık alanlarına özgü akademik soruları ve yanıtları içeren bir veri setinde eğitildi.
Eğitim Süreci: Ayarlama süreci, önceden eğitilmiş GPT-2 modelinin küratörlü veri setinde daha fazla eğitildiği denetimli öğrenme içermektedir ve bağlamsal anlayışını ve yanıt doğruluğunu artırmak için birçok farklı konfigürasyonla ayarlanmıştır.
####Türkçe Model
Model: Ayarlanmış ytu-ce-cosmos/turkish-gpt2
Veri Seti: Türkçe model, benzer akademik soruları ve yanıtları içeren ancak Türkçe dil bağlamlarına çevrilmiş ve uyarlanmış bir veri setinde eğitildi. Türkçe modelin karmaşık katmanları ve ağırlıkları, yanıt doğruluğu ve bağlamsal anlayış üzerinde etkili oldu!
Eğitim Süreci: İngilizce model gibi, Türkçe model de denetimli öğrenme tekniklerini ve farklı konfigürasyonları kullanarak, modelin ağırlıklarını ve karmaşık katmanlarını en iyi şekilde uyum sağlaması ve Türkçe'de bağlamsal olarak uygun yanıtlar üretme performansını artırmak için ayarlandı.

## İlgili Dosyalar

- **`QAapp.py`**: Sohbet robotu arayüzü için Streamlit uygulama kodunu içeren ana Python dosyası.
- **`question.py`**: Dil modellerini kullanarak soru-cevap yapmak için işlevleri tanımlayan Python dosyası.
- **`generate.py`**: Seçilen dile göre uygun belirteci ve dil modelini yüklemek için işlevler sağlayan Python dosyası.
- **`htmlTemplates.py`**: Sohbet robotu mesajlarını biçimlendirmek için HTML şablonlarını içeren Python dosyası.
- **`model_en`**: İngilizce dilinde soru-cevap için ayarlanmış OpenAI/gpt2 modeli.
- **`model_tr`**: Türkçe dilinde soru-cevap için ayarlanmış ytu-ce-cosmos/turkish-gpt2 modeli.
- **`requirements.txt`**: Projede gereken temel kütüphaneleri ve sürümlerini içerir.
