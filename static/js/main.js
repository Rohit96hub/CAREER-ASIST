document.addEventListener('DOMContentLoaded', () => {
    // --- STATE MANAGEMENT ---
    const user = {
        name: '',
        gender: '',
        career: null,
        careerIntroStep: 0,
        currentScenarioIndex: 0,
        personalScore: 0,
        communityScore: 0,
    };

    // --- DOM ELEMENTS ---
    const allPages = document.querySelectorAll('.page');
    const welcomeForm = document.getElementById('welcomeForm');
    const startBtn = document.getElementById('startBtn');
    const aboutBtn = document.getElementById('aboutBtn');
    const aboutBackBtn = document.getElementById('aboutBackBtn');
    const welcomeUserText = document.getElementById('welcomeUserText');
    const manualChoiceBtn = document.getElementById('manualChoiceBtn');
    const spinButton = document.getElementById('spinButton');
    
    // Modals
    const manualChoiceModal = document.getElementById('manualChoiceModal');
    const manualChoiceContent = document.getElementById('manualChoiceContent');
    const careerCongratsModal = document.getElementById('careerCongratsModal');
    const congratsContinueBtn = document.getElementById('congratsContinueBtn');
    
    // Narrative Pages & Content
    const narrativePage = document.getElementById('narrativePage');
    const narrativeBgImage = narrativePage.querySelector('.narrative-bg-image');
    const narrativeContentBox = narrativePage.querySelector('.narrative-content-box');

    const finalResultPage = document.getElementById('finalResultPage');
    const finalResultBgImage = finalResultPage.querySelector('.narrative-bg-image');
    const resultBox = document.getElementById('resultBox');
    
    // --- SOUNDS ---
    let masterVolume, selectSound, spinStartSound, reelStopSound, successSound;
    try {
        if (typeof Tone !== 'undefined') {
            masterVolume = new Tone.Volume(-12).toDestination(); // Approx 40% volume
            selectSound = new Tone.Synth({ oscillator: { type: 'sine' }, envelope: { attack: 0.01, decay: 0.2, sustain: 0.1, release: 0.1 } }).connect(masterVolume);
            //spinStartSound = new Tone.NoiseSynth({ noise: { type: 'pink' }, envelope: { attack: 0.01, decay: 1.5, sustain: 0.1 } }).connect(masterVolume);
            reelStopSound = new Tone.MembraneSynth({ pitchDecay: 0.02, octaves: 4, oscillator: { type: 'sine' } }).connect(masterVolume);
            successSound = new Tone.Synth({ oscillator: { type: 'triangle' }, envelope: { attack: 0.01, decay: 0.3, sustain: 0.1, release: 0.2 } }).connect(masterVolume);
        }
    } catch (e) {
        console.error("Tone.js not loaded, sounds disabled");
    }

    // --- UTILITY FUNCTIONS ---
    function playSound(sound, note = "C4", duration = "8n") {
        try {
            if (sound && typeof sound.triggerAttackRelease === 'function') {
                sound.triggerAttackRelease(note, duration);
            }
        } catch (e) {
            console.warn("Could not play sound", e);
        }
    }

    // --- PAGE NAVIGATION ---
    function showPage(pageId) {
        document.body.className = (pageId === 'welcomePage' || pageId === 'aboutPage') ? 'welcome-bg' : 'default-bg';
        
        allPages.forEach(page => {
            page.classList.remove('active');
            page.style.display = 'none';
        });

        const activePage = document.getElementById(pageId);
        if (activePage) {
            activePage.style.display = 'flex';
            
            setTimeout(() => {
                activePage.classList.add('active');
            }, 10);
        }
    }
    
    // --- EVENT LISTENERS ---
    startBtn.addEventListener('click', () => { 
        playSound(selectSound, "C4", "8n"); 
        showPage('nameGenderPage');  // FIXED: Changed from 'welcomePage' to 'nameGenderPage'
    });
    
    aboutBtn.addEventListener('click', () => { 
        playSound(selectSound, "C4", "8n"); 
        showPage('aboutPage'); 
    });
    
    aboutBackBtn.addEventListener('click', () => { 
        playSound(selectSound, "C4", "8n"); 
        showPage('welcomePage'); 
    });
    
    welcomeForm.addEventListener('submit', (e) => {
        e.preventDefault();
        user.name = document.getElementById('userName').value;
        user.gender = new FormData(welcomeForm).get('gender');
        if (user.name && user.gender) {
            welcomeUserText.textContent = `Welcome, ${user.name}!`;
            playSound(selectSound, "E4", "8n");
            showPage('careerSelectPage');
            setupSpinner();
        }
    });

    manualChoiceBtn.addEventListener('click', showManualChoice);
    
    // Career congrats modal
    congratsContinueBtn.addEventListener('click', () => {
        careerCongratsModal.classList.remove('visible');
        user.careerIntroStep = 0;
        renderNarrativeStep();
        showPage('narrativePage');
    });

    // --- CAREER SELECTION (MANUAL) ---
    function showManualChoice() {
        playSound(selectSound, "A4", "8n");
        const careerNames = Object.keys(CAREERS_DATA);
        manualChoiceContent.innerHTML = `
            <h2 class="text-3xl font-bold mb-6 text-center text-white">Choose Your Career</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                ${careerNames.map(name => {
                    const career = CAREERS_DATA[name].CareerCard;
                    return `<button class="manual-career-card" data-career="${name}">
                                <img src="${user.gender === 'male' ? career.AvatarMale : career.AvatarFemale}" alt="${name}" class="w-24 h-24 rounded-full mx-auto mb-3">
                                <h4 class="text-xl font-bold">${name}</h4>
                            </button>`;
                }).join('')}
            </div>
        `;
        manualChoiceModal.classList.add('visible');
        
        // Use event delegation for better performance
        manualChoiceContent.addEventListener('click', (e) => {
            const card = e.target.closest('.manual-career-card');
            if (card) {
                const careerName = card.dataset.career;
                startCareerJourney(careerName);
            }
        });
        
        manualChoiceModal.addEventListener('click', (e) => {
            if (e.target === manualChoiceModal) {
                manualChoiceModal.classList.remove('visible');
            }
        });
    }

    // --- THE JOURNEY BEGINS ---
    function startCareerJourney(careerName) {
        user.career = CAREERS_DATA[careerName];
        if (!user.career) {
            console.error("Invalid career selected:", careerName);
            return;
        }
        
        // Hide any open modals
        manualChoiceModal.classList.remove('visible');
        
        // Show congrats modal
        showCareerCongrats(careerName);
    }
    
    function showCareerCongrats(careerName) {
        const career = user.career.CareerCard;
        const avatarSrc = user.gender === 'male' ? career.AvatarMale : career.AvatarFemale;
        
        document.getElementById('careerNameSpan').textContent = careerName;
        document.getElementById('congratsAvatar').src = avatarSrc;
        document.getElementById('congratsTitle').textContent = `Congratulations, ${user.name}!`;
        document.getElementById('congratsMessage').innerHTML = `You've chosen to become a <span class="font-bold">${careerName}</span>!`;
        
        playSound(successSound, "C6", "0.5");
        careerCongratsModal.classList.add('visible');
    }

    // --- NARRATIVE ENGINE ---
    function renderNarrativeStep() {
        playSound(selectSound, "E5", "8n");
        const card = user.career.CareerCard;
        const images = user.career.Images;
        let contentHTML = '';
        let nextButtonText = 'Next';

        switch (user.careerIntroStep) {
            case 0: // Greeting
                narrativeBgImage.style.backgroundImage = `url('${images.Overview}')`;
                contentHTML = `<div><h3>Greetings, ${user.name}!</h3><p>You've chosen the path of a <strong>${card.Title}</strong>. ${card.Overview}</p></div>`;
                break;
            case 1: // Benefits & Challenges
                narrativeBgImage.style.backgroundImage = `url('${images.Benefits}')`;
                contentHTML = `<div><h3>Benefits & Challenges</h3><ul>${card.BenefitsAndChallenges.Benefits.map(b => `<li>${b}</li>`).join('')}</ul><h4 class="mt-4">Challenges</h4><ul>${card.BenefitsAndChallenges.JobChallenges.map(c => `<li>${c}</li>`).join('')}</ul></div>`;
                break;
            case 2: // Impact
                narrativeBgImage.style.backgroundImage = `url('${images.Impact}')`;
                contentHTML = `<div><h3>Your Potential Impact</h3><p><strong>Personal Growth:</strong> ${card.DualImpactHighlights.PersonalGrowth}</p><h4 class="mt-4">Community Impact</h4><p>${card.DualImpactHighlights.CommunityImpact}</p></div>`;
                nextButtonText = 'Make Your First Choice';
                break;
            default:
                renderInitialChoice();
                return;
        }
        
        narrativeContentBox.innerHTML = `<div>${contentHTML}</div><div class="text-right mt-6"><button id="narrativeNextBtn" class="btn-primary font-bold py-2 px-8 rounded-full">${nextButtonText}</button></div>`;
        
        // Use event delegation instead of direct assignment
        narrativeContentBox.querySelector('#narrativeNextBtn').addEventListener('click', () => {
            user.careerIntroStep++;
            renderNarrativeStep();
        });
    }

    function renderInitialChoice() {
        playSound(selectSound, "G5", "8n");
        const choice = user.career.InitialChoice;
        narrativeBgImage.style.backgroundImage = `url('${user.career.Images.InitialChoice}')`;
        narrativeContentBox.innerHTML = `
            <div>
                <h3>${choice.Question}</h3>
                <div class="grid md:grid-cols-2 gap-6 mt-6">
                    ${choice.Options.map(opt => `<button class="decision-card text-left" data-briefing="${opt.briefing}"><p class="font-semibold text-lg">${opt.text}</p></button>`).join('')}
                </div>
            </div>`;
        
        // Use event delegation
        narrativeContentBox.addEventListener('click', (e) => {
            const button = e.target.closest('.decision-card');
            if (button) {
                showBriefingAndContinue(button.dataset.briefing);
            }
        });
    }

    function showBriefingAndContinue(briefing) {
        playSound(selectSound, "C6", "8n");
        narrativeContentBox.innerHTML = `
            <div>
                <p class="text-lg italic">"${briefing}"</p>
                <p class="text-lg font-bold mt-6">You stand at a crossroads. Every choice you make will shape your journey! Are you ready to carve your path to success?</p>
                <div class="text-center mt-8">
                    <button id="startQuestBtn" class="btn-primary font-bold py-3 px-8 rounded-full text-lg">I'm Ready!</button>
                </div>
            </div>`;
            
        document.getElementById('startQuestBtn').addEventListener('click', startScenarios);
    }

    function startScenarios() {
        user.currentScenarioIndex = 0;
        user.personalScore = 0;
        user.communityScore = 0;
        renderScenario();
    }

    function renderScenario() {
        const scenario = user.career.Scenarios[user.currentScenarioIndex];
        if (!scenario) {
            showFinalResult();
            return;
        }
        
        narrativeBgImage.style.backgroundImage = `url('${user.career.Images[`Scenario${user.currentScenarioIndex + 1}`]}')`;
        
        let contentHTML = `
            <div>
                <h3>${scenario.Title}</h3>
                <p class="text-base md:text-lg mb-6">${scenario.Description}</p>
                <div class="grid md:grid-cols-2 gap-6">
                    ${scenario.DecisionCards.map(card => `
                        <button class="decision-card text-left" 
                                data-personal="${card.Outcomes.PersonalImpact}" 
                                data-community="${card.Outcomes.CommunityImpact}" 
                                data-feedback="${card.Feedback}">
                            <p class="font-semibold text-lg">${card.Option}</p>
                        </button>
                    `).join('')}
                </div>
            </div>`;
            
        narrativeContentBox.innerHTML = contentHTML;

        // Use event delegation
        narrativeContentBox.addEventListener('click', (e) => {
            const button = e.target.closest('.decision-card');
            if (button) {
                const outcomes = {
                    PersonalImpact: parseInt(button.dataset.personal),
                    CommunityImpact: parseInt(button.dataset.community)
                };
                makeDecision(outcomes, button.dataset.feedback);
            }
        });
    }

    function makeDecision(outcomes, feedback) {
        user.personalScore += outcomes.PersonalImpact;
        user.communityScore += outcomes.CommunityImpact;
        playSound(successSound, "A5", "8n");
        
        narrativeContentBox.innerHTML = `
             <div>
                <p class="text-lg italic">"${feedback}"</p>
                <div class="text-center mt-8">
                    <button id="scenarioNextBtn" class="btn-primary font-bold py-2 px-8 rounded-full">Continue</button>
                </div>
            </div>`;
        
        document.getElementById('scenarioNextBtn').addEventListener('click', () => {
            user.currentScenarioIndex++;
            renderScenario();
        });
    }

    function showFinalResult() {
        playSound(successSound, "C6", "0.5");
        const totalScore = user.personalScore + user.communityScore;
        const verdictKey = totalScore > 10 ? 'high' : totalScore > 5 ? 'medium' : 'low';
        const resultText = user.career.Verdicts[verdictKey].replace(/\bYou\b/g, `<strong>${user.name}</strong>`);
        
        finalResultBgImage.style.backgroundImage = `url('${user.career.Images.Result}')`;
        resultBox.innerHTML = `
            <h2 class="text-3xl font-bold text-[#f0c419] mb-4">Journey Complete!</h2>
            <p class="text-lg mb-6">${resultText}</p>
            <div class="text-xl font-semibold">
                <p>Final Personal Growth Score: <span class="text-white">${user.personalScore}</span></p>
                <p>Final Community Impact Score: <span class="text-white">${user.communityScore}</span></p>
            </div>
            <button id="restartGameBtn" class="btn-primary font-bold py-3 px-8 rounded-full text-lg mt-8">Play Again</button>
        `;
        
        showPage('finalResultPage');
        document.getElementById('restartGameBtn').addEventListener('click', () => window.location.reload());
    }

    // --- SPINNER LOGIC ---
    let reelElements, careerNames, isSpinning = false;
    
    function setupSpinner() {
        reelElements = document.querySelectorAll('#careerSelectPage .reel');
        careerNames = Object.keys(CAREERS_DATA);
        
        reelElements.forEach(reel => {
            reel.innerHTML = '';
            const reelInner = document.createElement('div');
            reelInner.className = 'reel-inner';
            
            // Create 3 copies of careers for smooth looping
            const items = [...careerNames, ...careerNames, ...careerNames].sort(() => 0.5 - Math.random());
            
            items.forEach(name => {
                const item = document.createElement('div');
                item.className = 'reel-item';
                const career = CAREERS_DATA[name].CareerCard;
                item.innerHTML = `<img src="${user.gender === 'male' ? career.AvatarMale : career.AvatarFemale}" 
                                      alt="${name}" 
                                      class="w-24 h-24 rounded-full"
                                      data-career="${name}">`;
                reelInner.appendChild(item);
            });
            
            reel.appendChild(reelInner);
        });
        
        spinButton.addEventListener('click', runSpinner);
    }
    
    function runSpinner() {
        if (isSpinning) return;
        isSpinning = true;
        
        // Change spin button to active state
        spinButton.src = "/static/images/spin_active.png";
        spinButton.classList.add('spinning');
        playSound(spinStartSound);
        
        // Get random career
        const resultCareerName = careerNames[Math.floor(Math.random() * careerNames.length)];
        
        reelElements.forEach((reel, index) => {
            const reelInner = reel.querySelector('.reel-inner');
            reel.classList.add('is-spinning');
            
            // Get career names from images in the reel
            const items = Array.from(reelInner.querySelectorAll('img')).map(img => img.dataset.career);
            
            setTimeout(() => {
                reel.classList.remove('is-spinning');
                
                // Find position of result career
                let targetIndex = items.findIndex(name => name === resultCareerName);
                if (targetIndex === -1) targetIndex = 0; // Fallback
                
                reelInner.style.transform = `translateY(-${targetIndex * 120}px)`;
                playSound(reelStopSound, "C2", "8n");

                if (index === reelElements.length - 1) {
                    // Release sound and finish spin
                    setTimeout(() => {
                        isSpinning = false;
                        spinButton.src = "/static/images/spin_normal.png";
                        spinButton.classList.remove('spinning');
                        
                        // Start career journey with result
                        startCareerJourney(resultCareerName);
                    }, 1500);
                }
            }, 1000 + index * 500);
        });
    }
});