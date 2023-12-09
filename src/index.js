
const chatbotConversation = document.getElementById('chatbot-conversation')
demo_queries = open("Course-Recommender\data\gpt_system_content.txt", "r", encoding="UTF-8").read()

//siia peaks lisama need kasutaja küssad ja chati vastused
const conversationArr = [
    {
        role: 'system',
        content: demo_queries
    }
] 

 document.addEventListener('submit', (e) => {
    e.preventDefault()
    const userInput = document.getElementById('user-input')
    conversationArr.push({ 
        role: 'user',
        content: userInput.value
    })
    //siin kutsuks välja selle vastuse saamise 
    //näidises oli see fetchReply() mille sees küsitakse openai'lt vastuse ja ss pushitakse conversationArr'i see

    const newSpeechBubble = document.createElement('div')
    newSpeechBubble.classList.add('speech', 'speech-human')
    chatbotConversation.appendChild(newSpeechBubble)
    newSpeechBubble.textContent = userInput.value
    userInput.value = ''
    chatbotConversation.scrollTop = chatbotConversation.scrollHeight
})

/*pmst see processQuery nagu pythonis aga tõlgitud js'i

const axios = require('axios');

async function processQuery(query, data) {
    // Check if query is a string
    if (typeof query !== 'string') {
        throw new Error("`query` should be a string");
    }

    let systemContentMessage = demoQueries + data;

    try {
        const response = await axios.post('https://api.openai.com/v1/engines/davinci-codex/completions', {
            deployment_id: "IDS2023_PIKANI_GPT35",
            model: "gpt-3.5-turbo",
            temperature: 0.0,  // Setting the temperature
            messages: [
                {role: "system", content: systemContentMessage},
                {role: "user", content: query}
            ]
        }, {
            headers: {
                'Authorization': `Bearer YOUR_OPENAI_API_KEY`,
                'Content-Type': 'application/json'
            }
        });

        let statusCode = response.data.choices[0].finish_reason;
        if (statusCode !== "stop") {
            throw new Error(`The status code was ${statusCode}.`);
        }

        return response.data.choices[0].message.content;
    } catch (error) {
        console.error("An error occurred:", error);
    }
}
*/ 

function renderTypewriterText(text) {
    const newSpeechBubble = document.createElement('div')
    newSpeechBubble.classList.add('speech', 'speech-ai', 'blinking-cursor')
    chatbotConversation.appendChild(newSpeechBubble)
    let i = 0
    const interval = setInterval(() => {
        newSpeechBubble.textContent += text.slice(i-1, i)
        if (text.length === i) {
            clearInterval(interval)
            newSpeechBubble.classList.remove('blinking-cursor')
        }
        i++
        chatbotConversation.scrollTop = chatbotConversation.scrollHeight
    }, 50)
}