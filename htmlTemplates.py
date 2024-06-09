css = '''
<style>
.chat-message {
    padding: 1.5rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
}

/* User message styling */
.chat-message.user {
    background-color: #2b313e;
    flex-direction: row-reverse;
}

/* Bot message styling */
.chat-message.bot {
    background-color: #475063;
    flex-direction: row;
}

/* Avatar styling */
.chat-message .avatar {
    width: 15%;
}

/* Avatar image styling */
.chat-message .avatar img {
    max-width: 78px;
    max-height: 78px;
    border-radius: 50%;
    object-fit: cover;
}

/* Message text styling */
.chat-message .message {
    width: 85%; /* telefon icin 85 yoksa 90 felan */
    padding: 0 1.5rem;
    color: #fff;
}

/* Bot message text alignment */
.chat-message.bot .message {
    text-align: left;
}

/* User message text alignment */
.chat-message.user .message {
    text-align: right;
}

@media (max-width: 768px) {
    .chat-message {
        flex-direction: column;
        align-items: flex-start;
    }
    
    .chat-message.user {
        flex-direction: column-reverse;
        align-items: flex-end;
    }
    
    .chat-message.bot {
        flex-direction: column-reverse;
        align-items: flex-end;
    }
    
    .chat-message .avatar {
        width: 20%;
    }

    .chat-message .message {
        width: 100%;
        padding: 0.5rem;
    }

    .chat-message .avatar img {
        max-width: 50px;
        max-height: 50px;
    }
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/34X0sb2/download.png">
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
