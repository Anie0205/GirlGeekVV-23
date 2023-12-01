function getChatbotResponse() {
    return new Promise(function(resolve, reject) {
        var Query = document.getElementById("query").value;
        const data = JSON.stringify({
            query: Query
        });

        const xhr = new XMLHttpRequest();
        xhr.withCredentials = true;

        xhr.addEventListener('readystatechange', function () {
            if (this.readyState === this.DONE) {
                const response = JSON.parse(this.responseText);
                resolve(response);
            }
        });

        xhr.open('POST', 'https://chatgpt-gpt4-ai-chatbot.p.rapidapi.com/ask');
        xhr.setRequestHeader('content-type', 'application/json');
        xhr.setRequestHeader('X-RapidAPI-Key', '1125161757msh4afefd5e6d850eep14cba2jsne8712c19895f');
        xhr.setRequestHeader('X-RapidAPI-Host', 'chatgpt-gpt4-ai-chatbot.p.rapidapi.com');

        xhr.send(data);
    }).then(function(response) {
        // Handle the response here
        var outputSection = document.getElementById("output");
        var outputContent = document.createElement("p");
        outputContent.textContent = response.response; // Assuming your API response contains a "response" field
        outputSection.appendChild(outputContent);
    }).catch(function(error) {
        // Handle any errors here
        console.error(error);
    });
}
