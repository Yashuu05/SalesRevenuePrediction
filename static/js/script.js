function switchTab(tab) {
    const btns = document.querySelectorAll('.tab-btn');
    btns.forEach(btn => btn.classList.remove('active'));

    if (tab === 'login') {
        btns[0].classList.add('active');
    } else {
        btns[1].classList.add('active');
    }
}

function handleAuth(event) {
    event.preventDefault();
    const btn = event.target.querySelector('button');
    const originalText = btn.innerText;

    // Simulate auth loading
    btn.innerHTML = 'Authenticating...';
    btn.disabled = true;

    setTimeout(() => {
        document.getElementById('auth-page').classList.remove('active');
        setTimeout(() => {
            document.getElementById('dashboard-page').classList.add('active');
            window.scrollTo(0, 0);
        }, 300);
    }, 1200);
}

function logout() {
    document.getElementById('dashboard-page').classList.remove('active');
    setTimeout(() => {
        document.getElementById('auth-page').classList.add('active');
        document.getElementById('auth-form').reset();
        const btn = document.getElementById('auth-form').querySelector('button');
        btn.innerHTML = 'Continue';
        btn.disabled = false;
    }, 300);
}

function handlePredict(event) {
    event.preventDefault();
    const resultCard = document.getElementById('result-card');
    const loader = document.getElementById('prediction-loader');
    const output = document.getElementById('prediction-output');

    resultCard.classList.remove('hidden');
    loader.classList.remove('hidden');
    output.classList.add('hidden');

    // Scroll to result on mobile
    if (window.innerWidth < 968) {
        resultCard.scrollIntoView({ behavior: 'smooth' });
    }

    // Simulate 3 seconds of "prediction"
    setTimeout(() => {
        loader.classList.add('hidden');
        output.classList.remove('hidden');

        // Generate fake data
        const fakeRevenue = (Math.random() * 50000 + 10000).toLocaleString(undefined, {
            minimumFractionDigits: 2,
            maximumFractionDigits: 2
        });
        const fakeProb = Math.floor(Math.random() * 20 + 75); // 75-95%

        // Animate results
        animateValue("revenue-amount", 0, parseFloat(fakeRevenue.replace(/,/g, '')), 1500);

        const probFill = document.getElementById('prob-fill');
        const probVal = document.getElementById('prob-val');

        setTimeout(() => {
            probFill.style.width = fakeProb + '%';
            probVal.innerText = fakeProb + '%';
        }, 100);

    }, 3000);
}

function resetForm() {
    document.getElementById('prediction-form').reset();
    document.getElementById('result-card').classList.add('hidden');
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function animateValue(id, start, end, duration) {
    const obj = document.getElementById(id);
    let startTimestamp = null;
    const step = (timestamp) => {
        if (!startTimestamp) startTimestamp = timestamp;
        const progress = Math.min((timestamp - startTimestamp) / duration, 1);
        const currentVal = (progress * (end - start)).toFixed(2);
        obj.innerHTML = parseFloat(currentVal).toLocaleString(undefined, {
            minimumFractionDigits: 2,
            maximumFractionDigits: 2
        });
        if (progress < 1) {
            window.requestAnimationFrame(step);
        }
    };
    window.requestAnimationFrame(step);
}
