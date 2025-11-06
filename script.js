// ⚠️ IMPORTANT: After deploying backend, replace this URL with your backend URL
// Example: const BACKEND_URL = "https://your-backend-name.onrender.com/submit";
const BACKEND_URL = "REPLACE_WITH_YOUR_BACKEND_URL/submit";

// State
let testStartTime;
let timerInterval;
const TEST_DURATION = 1200; // 20 minutes in seconds
let timeRemaining = TEST_DURATION;

// DOM Elements
const loginForm = document.getElementById('loginForm');
const testInterface = document.getElementById('testInterface');
const confirmationMessage = document.getElementById('confirmationMessage');
const startTestBtn = document.getElementById('startTestBtn');
const testForm = document.getElementById('testForm');
const timerDisplay = document.getElementById('timerDisplay');
const candidateNameInput = document.getElementById('candidateName');
const mobileNumberInput = document.getElementById('mobileNumber');
const mobileError = document.getElementById('mobileError');

// Validate mobile number
function validateMobileNumber(mobile) {
    const mobileRegex = /^[0-9]{10}$/;
    return mobileRegex.test(mobile);
}

// Format time for display
function formatTime(seconds) {
    const minutes = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${minutes.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
}

// Update timer display
function updateTimer() {
    timeRemaining--;
    timerDisplay.textContent = formatTime(timeRemaining);

    // Change color based on time remaining
    const timerElement = document.querySelector('.timer');
    if (timeRemaining <= 60) {
        timerElement.classList.add('danger');
        timerElement.classList.remove('warning');
    } else if (timeRemaining <= 300) {
        timerElement.classList.add('warning');
        timerElement.classList.remove('danger');
    }

    // Auto-submit when time runs out
    if (timeRemaining <= 0) {
        clearInterval(timerInterval);
        submitTest(true);
    }
}

// Start test
startTestBtn.addEventListener('click', () => {
    const name = candidateNameInput.value.trim();
    const mobile = mobileNumberInput.value.trim();

    // Validate inputs
    if (!name) {
        alert('Please enter your name');
        return;
    }

    if (!validateMobileNumber(mobile)) {
        mobileError.textContent = 'Please enter a valid 10-digit mobile number';
        return;
    }

    // Clear error and start test
    mobileError.textContent = '';
    loginForm.classList.add('hidden');
    testInterface.classList.remove('hidden');

    // Start timer
    testStartTime = new Date();
    timerInterval = setInterval(updateTimer, 1000);
});

// Submit test
testForm.addEventListener('submit', (e) => {
    e.preventDefault();
    submitTest(false);
});

async function submitTest(autoSubmit) {
    // Stop timer
    clearInterval(timerInterval);

    // Collect answers
    const answers = {
        Q1: document.getElementById('answer1').value.trim(),
        Q2: document.getElementById('answer2').value.trim(),
        Q3: document.getElementById('answer3').value.trim(),
        Q4: document.getElementById('answer4').value.trim(),
        Q5: document.getElementById('answer5').value.trim()
    };

    // Disable all inputs
    document.querySelectorAll('textarea').forEach(textarea => {
        textarea.disabled = true;
    });
    document.getElementById('submitBtn').disabled = true;

    // Prepare submission data
    const submissionData = {
        name: candidateNameInput.value.trim(),
        mobile: mobileNumberInput.value.trim(),
        answers: answers,
        submission_time: new Date().toISOString(),
        time_taken_seconds: TEST_DURATION - timeRemaining
    };

    try {
        // Send to backend
        const response = await fetch(BACKEND_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(submissionData)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        console.log('Submission successful:', result);

        // Show confirmation
        testInterface.classList.add('hidden');
        confirmationMessage.classList.remove('hidden');

    } catch (error) {
        console.error('Submission error:', error);
        alert('Submission recorded locally. Please inform the administrator if this error persists.');
        
        // Still show confirmation even if backend fails
        testInterface.classList.add('hidden');
        confirmationMessage.classList.remove('hidden');
    }
}

// Prevent accidental page refresh
window.addEventListener('beforeunload', (e) => {
    if (testInterface && !testInterface.classList.contains('hidden')) {
        e.preventDefault();
        e.returnValue = '';
    }
});

