
document.getElementById("predictForm").addEventListener("submit",async function (e) {
    e.preventDefault()

    const Sex = document.getElementById("sex").value
    const data = {
        Pclass: parseInt(document.getElementById("pclass").value),
        Age: parseFloat(document.getElementById("age").value),
        SibSp : parseInt(document.getElementById("sibsp").value),
        Parch : parseInt(document.getElementById("parch").value),
        Fare : parseFloat(document.getElementById("fare").value),
        Sex_female: Sex === "female" ? 1:0,
        Sex_male: Sex==="male" ? 1:0

    }

    const resultPlace = document.getElementById("result");


    try{
        
    const API_URL = "https://titanic-predictor-model.onrender.com/predict"
    const response = await fetch(API_URL,{
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    })

        const result = await response.json()

        if (result.prediction == "Survived"){
            resultPlace.innerHTML=`<p>Survived (${(result.probability_survived).toFixed(1)*100}%)</p>`
        }
        else{
            resultPlace.innerHTML=`<p>Did not survive (${(result.probability_not_survived).toFixed(1)*100}%)</p>`
        }

    }

    catch(error){
        resultPlace.innerHTML=`<p>Something went wrong!</p>`
        console.log(error)
    }
})
