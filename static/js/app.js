// Language Translation

function changeLanguage(lang){

    localStorage.setItem("language", lang);

    const englishBtn =
        document.getElementById("englishBtn");

    const hindiBtn =
        document.getElementById("hindiBtn");

    englishBtn.classList.remove("active");
    hindiBtn.classList.remove("active");

    if(lang === "en"){
        englishBtn.classList.add("active");
    }else{
        hindiBtn.classList.add("active");
    }

    document.getElementById("hero-title").innerText =
        translations[lang].hero_title;

    document.getElementById("hero-subtitle").innerText =
        translations[lang].hero_subtitle;

    document.getElementById("profile-title").innerText =
        translations[lang].profile;

    document.getElementById("age-label").innerText =
        translations[lang].age;

    document.getElementById("income-label").innerText =
        translations[lang].income;

    document.getElementById("occupation-label").innerText =
        translations[lang].occupation;

    document.getElementById("state-label").innerText =
        translations[lang].state;

    document.getElementById("gender-label").innerText =
        translations[lang].gender;

    document.getElementById("category-label").innerText =
        translations[lang].category;

    document.getElementById("find-btn").innerText =
        translations[lang].button;

    document.getElementById("feature-eligibility").innerText =
        translations[lang].eligibility;

    document.getElementById("feature-search").innerText =
        translations[lang].search;

    document.getElementById("feature-advisor").innerText =
        translations[lang].advisor;

    document.getElementById("cat-farmers").innerText =
        translations[lang].farmers;

    document.getElementById("cat-healthcare").innerText =
        translations[lang].healthcare;

    document.getElementById("cat-business").innerText =
        translations[lang].business;

    document.getElementById("cat-students").innerText =
        translations[lang].students;

    document.getElementById("cat-youth").innerText =
        translations[lang].youth;

    document.getElementById("cat-housing").innerText =
        translations[lang].housing;

    document.getElementById("cat-women").innerText =
        translations[lang].women;
    
    document.getElementById("age-input").placeholder =
    translations[lang].age_placeholder;

    document.getElementById("income-input").placeholder =
    translations[lang].income_placeholder;

    document.getElementById("active-schemes-text").innerText =
    translations[lang].active_schemes;

    document.getElementById("health-cover-text").innerText =
    translations[lang].health_cover;

    document.getElementById("match-time-text").innerText =
    translations[lang].match_time;

    const occupationSelect =
document.getElementById("occupation-select");

if(lang === "hi"){

    occupationSelect.innerHTML = `
        <option>चुनें...</option>
        <option>छात्र</option>
        <option>किसान</option>
        <option>व्यवसाय</option>
        <option>कर्मचारी</option>
    `;

}else{

    occupationSelect.innerHTML = `
        <option>Select...</option>
        <option>Student</option>
        <option>Farmer</option>
        <option>Business</option>
        <option>Employee</option>
    `;
}

const stateSelect =
document.getElementById("state-select");

if(lang === "hi"){

    stateSelect.innerHTML = `
        <option>चुनें...</option>
        <option>मध्य प्रदेश</option>
        <option>महाराष्ट्र</option>
        <option>राजस्थान</option>
    `;

}else{

    stateSelect.innerHTML = `
        <option>Select...</option>
        <option>Madhya Pradesh</option>
        <option>Maharashtra</option>
        <option>Rajasthan</option>
    `;
}
const genderSelect =
document.getElementById("gender-select");

if(lang === "hi"){

    genderSelect.innerHTML = `
        <option>चुनें...</option>
        <option>पुरुष</option>
        <option>महिला</option>
    `;

}else{

    genderSelect.innerHTML = `
        <option>Select...</option>
        <option>Male</option>
        <option>Female</option>
    `;
}
const categorySelect =
document.getElementById("category-select");

if(lang === "hi"){

    categorySelect.innerHTML = `
        <option>चुनें...</option>
        <option>सामान्य</option>
        <option>ओबीसी</option>
        <option>एससी</option>
        <option>एसटी</option>
    `;

}else{

    categorySelect.innerHTML = `
        <option>Select...</option>
        <option>General</option>
        <option>OBC</option>
        <option>SC</option>
        <option>ST</option>
    `;
}
}


document
.getElementById("englishBtn")
.addEventListener("click", () => {

    changeLanguage("en");

});


document
.getElementById("hindiBtn")
.addEventListener("click", () => {

    changeLanguage("hi");

});


window.onload = () => {

    const language =
        localStorage.getItem("language") || "en";

    changeLanguage(language);
};

// Data 
const form =
document.getElementById("profileForm");

form.addEventListener("submit", async (e) => {

    e.preventDefault();

    const income =
    Number(document.getElementById("income-input").value);

    const occupation =
    document.getElementById("occupation-select").value;

    console.log("Occupation:", occupation);
    console.log("Income:", income);
    const response =
    await fetch("/find-schemes", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({

            age: Number(
            document.getElementById("age-input").value
            ),

            income: Number(
                document.getElementById("income-input").value
            ),

            occupation:
                document.getElementById("occupation-select").value,

            gender:
                document.getElementById("gender-select").value,

            category:
                document.getElementById("category-select").value,

            state:
                document.getElementById("state-select").value

        })
    });

    const data = await response.json();

    console.log("Schemes received:", data);

    displaySchemes(data);
});

// Show Result

// function displaySchemes(schemes){
//     console.log("displaySchemes called");
//     console.log(schemes);
//     document.getElementById("results").style.display = "block";

//     const count = schemes.length;

//     document.getElementById("results-title").innerText =
//     `${count} Eligible Scheme${count > 1 ? 's' : ''} Found`;

//     setTimeout(() => {

//         document.getElementById("results").scrollIntoView({
//             behavior: "smooth",
//             block: "start"
//         });

//     }, 100);

//     const results =
//     document.getElementById("resultsContainer");

//     results.innerHTML = "";

//     if(schemes.length === 0){

//         results.innerHTML =
//         "<p>No eligible schemes found.</p>";

//         return;
//     }

//     schemes.forEach(scheme => {

//         const benefits =
//         scheme.benefits
//         .map(item => `<li>${item}</li>`)
//         .join("");

//         const documents =
//         scheme.documents
//         .map(doc => `<li>${doc}</li>`)
//         .join("");

//         results.innerHTML += `
//         <div class="scheme-card">

//             <h3>${scheme.name}</h3>

//             <h4>Benefits</h4>

//             <ul>
//                 ${benefits}
//             </ul>

//             <h4>Required Documents</h4>

//             <ul>
//                 ${documents}
//             </ul>

//             <a
//                 href="${scheme.apply_link}"
//                 target="_blank"
//                 class="apply-btn">

//                 Apply Now

//             </a>

//         </div>
//         `;
//     });
// }

function displaySchemes(schemes){

    document.getElementById("results").style.display = "block";

    const count = schemes.length;

    document.getElementById("results-title").innerText =
        `${count} Eligible Scheme${count > 1 ? "s" : ""} Found`;

    const results =
        document.getElementById("resultsContainer");

    results.innerHTML = "";

    if(schemes.length === 0){

        results.innerHTML =
            "<p>No schemes found.</p>";

        return;
    }

    schemes.forEach(scheme => {

        // OLD JSON (eligibility checker)
        if(scheme.documents){

            const benefits =
                (scheme.benefits || [])
                .map(item => `<li>${item}</li>`)
                .join("");

            const documents =
                (scheme.documents || [])
                .map(doc => `<li>${doc}</li>`)
                .join("");

            results.innerHTML += `

            <div class="scheme-card">

                <h3>${scheme.name}</h3>

                <h4>Benefits</h4>

                <ul>${benefits}</ul>

                <h4>Required Documents</h4>

                <ul>${documents}</ul>

                <a href="${scheme.apply_link}"
                   target="_blank"
                   class="apply-btn">

                    Apply Now

                </a>

            </div>

            `;

        }

        // SCRAPED JSON (search)
        else{

            const benefits =
                (scheme.benefits || [])
                .map(item => `<li>${item}</li>`)
                .join("");

            const eligibility =
                (scheme.eligibility || [])
                .map(item => `<li>${item}</li>`)
                .join("");

            results.innerHTML += `

            <div class="scheme-card">

                <h3>${scheme.name}</h3>

                <p><b>Ministry:</b> ${scheme.ministry || "N/A"}</p>

                <p>${scheme.description || ""}</p>

                <h4>Benefits</h4>

                <ul>${benefits}</ul>

                <h4>Eligibility</h4>

                <ul>${eligibility}</ul>

                <a href="${scheme.official_link}"
                   target="_blank"
                   class="apply-btn">

                    Official Website

                </a>

            </div>

            `;
        }

    });
    setTimeout(() => {
        document.getElementById("results").scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
    }, 100);

}
    document
    .getElementById("searchBtn")
    .addEventListener("click", async () => {
        console.log("Search button clicked");
        const keyword =
        document
        .getElementById("searchInput")
        .value;

        const response =
        await fetch("/search-schemes", {

            method: "POST",

            headers: {
                "Content-Type":
                "application/json"
            },

            body: JSON.stringify({
                keyword
            })
        });

        const data =
        await response.json();
        console.log("Search Results:", data);
        displaySchemes(data);
        
    });


document
.getElementById("askAiBtn")
.addEventListener("click", async () => {

    const question =
    document
    .getElementById("aiQuestion")
    .value;

    if(!question){
        alert("Please enter a question");
        return;
    }

    document
    .getElementById("aiResponse")
    .innerHTML = "Thinking...";

    const response =
    await fetch("/ask-ai", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            question:
            document.getElementById("aiQuestion").value,
            age: Number(
            document.getElementById("age-input").value),

            income:Number(
            document.getElementById("income-input").value),

            occupation:
            document.getElementById("occupation-select").value,

            gender:
            document.getElementById("gender-select").value,

            category:
            document.getElementById("category-select").value,

            state:
            document.getElementById("state-select").value

        })
    });

    const data =
    await response.json();

    document
    .getElementById("aiResponse")
    .innerHTML = marked.parse(data.answer);
});