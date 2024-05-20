css = '''
<style>
.chat-message {
    padding: 1.5rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
}
.chat-message.user {
    background-color: #2b313e;
    flex-direction: row-reverse;
}
.chat-message.bot {
    background-color: #475063;
    flex-direction: row;
}
.chat-message .avatar {
    width: 10%;
}
.chat-message .avatar img {
    max-width: 78px;
    max-height: 78px;
    border-radius: 50%;
    object-fit: cover;
}
.chat-message .message {
    width: 90%;
    padding: 0 1.5rem;
    color: #fff;
}
.chat-message.bot .message {
    text-align: left;
}
.chat-message.user .message {
    text-align: right;
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/34X0sb2/download.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/zx8gf4Q/download-1.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
