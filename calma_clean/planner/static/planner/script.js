// (function() {
//     const moodSlider = document.getElementById('mood');
//     const moodEmoji = document.getElementById('mood-emoji');

//     if (moodSlider && moodEmoji) {
//         const moodMap = {
//             1: "😞",
//             2: "😕",
//             3: "😐",
//             4: "😊",
//             5: "😄"
//         };

//         moodSlider.addEventListener('input', () => {
//             const val = moodSlider.value;
//             moodEmoji.textContent = moodMap[val];
//             moodSlider.style.background = `linear-gradient(to right, #26a69a ${val*20}%, #ccc ${val*20}%)`;
//         });
//     }


//     const form = document.getElementById("checkin-form");
//     const aiBox = document.querySelector(".ai-box");

//     if (form && aiBox) {
//         form.addEventListener("submit", function (e) {
//             e.preventDefault();
//             const formData = new FormData(form);

//             fetch("/planner/ai-feedback/", {
//                 method: "POST",
//                 headers: {
//                     "X-CSRFToken": formData.get("csrfmiddlewaretoken"),
//                 },
//                 body: formData,
//             })
//             .then(response => response.json())
//             .then(data => {
//                 aiBox.innerText = data.feedback || "🤖 No feedback available";
//                 form.submit();
//             })
//             .catch(err => {
//                 console.error("AI feedback error:", err);
//                 form.submit();
//             });
//         });
//     }
// })();

// document.addEventListener("DOMContentLoaded", function () {

//     const energySlider = document.getElementById("energy");
//     const energyValue = document.getElementById("energy-value");

//     if (!energySlider || !energyValue) {
//         console.log("Energy elements not found");
//         return;
//     }

//     // initial value
//     energyValue.textContent = energySlider.value;

//     energySlider.addEventListener("input", function () {
//         energyValue.textContent = energySlider.value;
//     });

// });

// const form = document.getElementById("checkin-form");
// const aiBox = document.getElementById("ai-box");

// form.addEventListener("submit", function(e) {
//     e.preventDefault(); // منع reload

//     const formData = new FormData(form);

//     fetch("{% url 'ai-feedback/' %}", {
//         method: "POST",
//         headers: {
//             "X-CSRFToken": formData.get("csrfmiddlewaretoken")
//         },
//         body: formData
//     })
//     .then(res => res.json())
//     .then(data => {
//         aiBox.innerText = data.feedback || "🤖 No feedback available";
//         form.submit(); // بعد ما تجي الـ AI نرسل البيانات للداتابيز
//     });
// });

document.addEventListener("DOMContentLoaded", function () {
    // -------- Mood Slider --------
    const moodSlider = document.getElementById("mood");
    const moodEmoji = document.getElementById("mood-emoji");

    if (moodSlider && moodEmoji) {
        const moodMap = {
            1: "😞",
            2: "😕",
            3: "😐",
            4: "😊",
            5: "😄"
        };

        moodSlider.addEventListener("input", () => {
            const val = moodSlider.value;
            moodEmoji.textContent = moodMap[val];
            moodSlider.style.background = `linear-gradient(to right, #26a69a ${val*20}%, #ccc ${val*20}%)`;
        });
    }

    // -------- Energy Slider --------
    const energySlider = document.getElementById("energy");
    const energyValue = document.getElementById("energy-value");

    if (energySlider && energyValue) {
        energyValue.textContent = energySlider.value;
        energySlider.addEventListener("input", () => {
            energyValue.textContent = energySlider.value;
            energySlider.style.background = `linear-gradient(to right, #ff9800 ${energySlider.value*10}%, #ccc ${energySlider.value*10}%)`;
        });
    }

    // -------- Form & AI Feedback --------
const form = document.getElementById("checkin-form");
const aiBox = document.getElementById("ai-box");

form.addEventListener("submit", function(e) {
    e.preventDefault(); // يمنع reload

    const formData = new FormData(form);

    fetch("{% url 'ai_feedback_api' %}", {
        method: "POST",
        headers: {
            "X-CSRFToken": formData.get("csrfmiddlewaretoken")
        },
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        aiBox.innerText = data.feedback || "🤖 No feedback available";
        // تحديث الجدول بالـ JS أو reload لو حابة
        location.reload();
    })
    .catch(err => {
        console.error(err);
        form.submit(); // fallback
    });
});
});

const aiBox = document.getElementById("ai-box");

function showLoader() {
    aiBox.innerHTML = '<div class="loader"></div>';
}

function hideLoader(feedback) {
    aiBox.innerHTML = feedback;
}

// مثال عند إرسال البيانات
form.addEventListener("submit", function(e){
    e.preventDefault();
    showLoader();
    const formData = new FormData(form);

    fetch("/planner/ai-feedback/", {
        method: "POST",
        headers: {"X-CSRFToken": formData.get("csrfmiddlewaretoken")},
        body: formData
    })
    .then(res => res.json())
    .then(data => hideLoader(data.feedback || "🤖 No feedback available"))
    .catch(err => hideLoader("🤖 Error fetching feedback"));
});
