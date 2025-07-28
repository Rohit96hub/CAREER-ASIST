# career-finder/career_data.py

CAREERS = {
    "Doctor": {
        "CareerCard": {
            "Title": "Doctor",
            "Stream": "Healthcare",
            "AvatarMale": "/static/images/doctor_avatar_male.png",
            "AvatarFemale": "/static/images/doctor_avatar_female.png",
            "Overview": "As a Doctor, you are a pillar of health and hope in your community. You dedicate your life to diagnosing and treating illnesses, using your vast knowledge to mend the body and comfort the mind.",
            "BenefitsAndChallenges": {
                "Benefits": [
                    "Profound sense of purpose and fulfillment.",
                    "High earning potential and strong job security.",
                    "Engages in continuous learning and professional development."
                ],
                "JobChallenges": [
                    "Long and rigorous education and training.",
                    "High levels of stress and emotional responsibility.",
                    "Irregular hours that can impact personal life."
                ]
            },
            "DualImpactHighlights": {
                "PersonalGrowth": "Fosters deep empathy, sharpens critical problem-solving skills, and builds resilience under pressure, leading to immense personal accomplishment.",
                "CommunityImpact": "Directly improves public health, educates communities on wellness, and enhances the quality of life for countless individuals."
            }
        },
        "Images": {
            "Overview": "/static/images/doctor/overview.png",
            "Benefits": "/static/images/doctor/benefits.png",
            "Impact": "/static/images/doctor/impact.png",
            "InitialChoice": "/static/images/doctor/choice.png",
            "Scenario1": "/static/images/doctor/scenario1.png",
            "Scenario2": "/static/images/doctor/scenario2.png",
            "Result": "/static/images/doctor/result.png"
        },
        "Audio": {
            "Overview": "/static/audio/doctor/overview.mp3",
            "Benefits": "/static/audio/doctor/benefits.mp3",
            "Impact": "/static/audio/doctor/impact.mp3",
            "InitialChoice": "/static/audio/doctor/initial_choice.mp3",
            "Scenario1": "/static/audio/doctor/scenario1.mp3",
            "Scenario2": "/static/audio/doctor/scenario2.mp3",
            "Result": "/static/audio/doctor/result.mp3"
        },
        "InitialChoice": {
            "Question": "How will you begin your journey as a Doctor?",
            "Options": [
                {
                    "type": "Personal",
                    "text": "Focus on specializing in a complex surgical field.",
                    "briefing": "An excellent choice. By honing your personal skills to the highest level, you aim to become a renowned expert, capable of performing life-saving procedures that few others can."
                },
                {
                    "type": "Community",
                    "text": "Join a public health initiative to combat epidemics.",
                    "briefing": "A noble path. You've chosen to focus on the bigger picture, working to protect entire communities from widespread disease and improve the health of thousands."
                }
            ]
        },
        "Scenarios": [
            {
                "Level": 1,
                "Title": "First Day at the Clinic",
                "Description": "It's your first day in a busy outpatient clinic. The waiting room is full, and every patient presents a unique challenge. How do you approach the day?",
                "DecisionCards": [
                    {
                        "Option": "Take extra time with each patient, ensuring you understand their full history, even if it puts you behind schedule.",
                        "Outcomes": {"PersonalImpact": 4, "CommunityImpact": 6},
                        "Feedback": "Your thoroughness is commendable. While your schedule suffers, the quality of care you provide builds deep trust with your patients."
                    },
                    {
                        "Option": "Be efficient and quick, adhering strictly to the schedule to see as many patients as possible.",
                        "Outcomes": {"PersonalImpact": 2, "CommunityImpact": 3},
                        "Feedback": "Your efficiency is impressive, allowing the clinic to serve more people. However, some patients may feel their concerns were not fully heard."
                    }
                ]
            },
            {
                "Level": 2,
                "Title": "Leading a Critical Care Team",
                "Description": "You're now an experienced physician leading a team during a mass-casualty event. The ER is in chaos. Your leadership is crucial.",
                "DecisionCards": [
                    {
                        "Option": "Trust your team. Delegate tasks based on each member's strengths and focus on coordinating the overall response.",
                        "Outcomes": {"PersonalImpact": 3, "CommunityImpact": 5},
                        "Feedback": "A true leader! By empowering your team, you multiply your effectiveness, saving more lives than you ever could alone."
                    },
                    {
                        "Option": "Take control of the most critical cases yourself, believing your hands are the most reliable.",
                        "Outcomes": {"PersonalImpact": -4, "CommunityImpact": -5},
                        "Feedback": "While your skill is undeniable, trying to do everything yourself creates bottlenecks and demoralizes your team, leading to poorer outcomes overall."
                    }
                ]
            }
        ],
        "Verdicts": {
            "high": "Your journey as a Doctor has been nothing short of legendary. You've balanced profound medical skill with deep compassion, becoming a pillar of healing in your community. Your name is spoken with hope and respect.",
            "medium": "You have proven yourself to be a capable and dedicated Doctor. You've saved lives and improved the well-being of many. Continue to hone your instincts and leadership, and your impact will only grow.",
            "low": "The path of a Doctor is fraught with challenge. While you've shown promise, your journey has highlighted areas for growth in balancing personal skill with community need. Every great healer's journey begins with learning."
        }
    },
    "IAS Officer": {
        "CareerCard": {
            "Title": "IAS Officer",
            "Stream": "Civil Services",
            "AvatarMale": "/static/images/ias_avatar_male.png",
            "AvatarFemale": "/static/images/ias_avatar_female.png",
            "Overview": "As an Indian Administrative Service officer, you'll be at the forefront of governance, implementing policies, managing public resources, and driving socio-economic development across districts and ministries.",
            "BenefitsAndChallenges": {
                "Benefits": [
                    "Unparalleled authority to create systemic change",
                    "Job security with lifelong prestige and respect",
                    "Diverse exposure across governance domains"
                ],
                "JobChallenges": [
                    "Political pressure and bureaucratic complexities",
                    "High public scrutiny with 24/7 accountability",
                    "Frequent transfers disrupting personal life"
                ]
            },
            "DualImpactHighlights": {
                "PersonalGrowth": "Develops exceptional leadership, crisis management, and strategic decision-making abilities through complex governance challenges.",
                "CommunityImpact": "Directly transforms communities through policy implementation, infrastructure development, and public welfare initiatives."
            }
        },
        "Images": {
            "Overview": "/static/images/ias/overview.png",
            "Benefits": "/static/images/ias/benefits.png",
            "Impact": "/static/images/ias/impact.png",
            "InitialChoice": "/static/images/ias/choice.png",
            "Scenario1": "/static/images/ias/scenario1.png",
            "Scenario2": "/static/images/ias/scenario2.png",
            "Result": "/static/images/ias/result.png"
        },
        "Audio": {
            "Overview": "/static/audio/ias/overview.mp3",
            "Benefits": "/static/audio/ias/benefits.mp3",
            "Impact": "/static/audio/ias/impact.mp3",
            "InitialChoice": "/static/audio/ias/initial_choice.mp3",
            "Scenario1": "/static/audio/ias/scenario1.mp3",
            "Scenario2": "/static/audio/ias/scenario2.mp3",
            "Result": "/static/audio/ias/result.mp3"
        },
        "InitialChoice": {
            "Question": "What will be your administrative philosophy?",
            "Options": [
                {
                    "type": "Personal",
                    "text": "Focus on policy innovation and systemic reforms",
                    "briefing": "You'll drive transformative changes by redesigning governance frameworks and creating model systems for others to follow."
                },
                {
                    "type": "Community",
                    "text": "Prioritize grassroots implementation and public service delivery",
                    "briefing": "You'll ensure government schemes reach the most vulnerable populations through rigorous field monitoring and community engagement."
                }
            ]
        },
        "Scenarios": [
            {
                "Level": 1,
                "Title": "District Crisis Management",
                "Description": "Flash floods have devastated your district during monsoon season. Thousands are stranded without food/water while critical infrastructure is damaged.",
                "DecisionCards": [
                    {
                        "Option": "Mobilize all departments under disaster protocol and personally oversee rescue operations",
                        "Outcomes": {"PersonalImpact": 5, "CommunityImpact": 8},
                        "Feedback": "Your hands-on leadership saved countless lives and established efficient coordination between agencies."
                    },
                    {
                        "Option": "Delegate to departments while focusing on long-term rehabilitation planning",
                        "Outcomes": {"PersonalImpact": 3, "CommunityImpact": 4},
                        "Feedback": "While recovery planning is strong, immediate relief efforts suffered from lack of field coordination."
                    }
                ]
            },
            {
                "Level": 2,
                "Title": "Corruption Allegation",
                "Description": "A major development project you approved faces corruption charges. Political pressure mounts to clear the contractor while activists demand cancellation.",
                "DecisionCards": [
                    {
                        "Option": "Order independent audit and freeze payments pending investigation",
                        "Outcomes": {"PersonalImpact": 7, "CommunityImpact": 6},
                        "Feedback": "Your transparent approach maintained public trust while establishing accountability mechanisms."
                    },
                    {
                        "Option": "Fast-track completion to avoid cost overruns while quietly investigating",
                        "Outcomes": {"PersonalImpact": -4, "CommunityImpact": -6},
                        "Feedback": "Perceived cover-up damaged institutional credibility and eroded public confidence in governance."
                    }
                ]
            }
        ],
        "Verdicts": {
            "high": "You've embodied the steel frame of India with integrity and vision. Your reforms have transformed governance while your compassion uplifted millions.",
            "medium": "A competent officer who delivered essential services. With more courageous decisions, your impact could reach transformative levels.",
            "low": "The bureaucracy proved challenging. Reconnect with public service ideals to turn challenges into opportunities for growth."
        }
    },
    "IPS Officer": {
        "CareerCard": {
            "Title": "IPS Officer",
            "Stream": "Civil Services",
            "AvatarMale": "/static/images/ips_avatar_male.png",
            "AvatarFemale": "/static/images/ips_avatar_female.png",
            "Overview": "As an Indian Police Service officer, you'll maintain law and order, prevent crimes, lead police forces, and ensure justice while navigating complex socio-political landscapes.",
            "BenefitsAndChallenges": {
                "Benefits": [
                    "Authority to ensure justice and social harmony",
                    "Dynamic field operations with leadership opportunities",
                    "Respect as symbol of state authority"
                ],
                "JobChallenges": [
                    "Life-threatening risks during operations",
                    "Balancing political pressures with professional integrity",
                    "Managing public expectations with limited resources"
                ]
            },
            "DualImpactHighlights": {
                "PersonalGrowth": "Develops exceptional crisis management, tactical decision-making, and emotional resilience in high-stakes situations.",
                "CommunityImpact": "Creates safer communities through crime prevention, upholds rule of law, and builds public trust in justice systems."
            }
        },
        "Images": { 
            "Overview": "/static/images/ips/overview.png",
            "Benefits": "/static/images/ips/benefits.png",
            "Impact": "/static/images/ips/impact.png",
            "InitialChoice": "/static/images/ips/choice.png",
            "Scenario1": "/static/images/ips/scenario1.png",
            "Scenario2": "/static/images/ips/scenario2.png",
            "Result": "/static/images/ips/result.png"
        },
        "Audio": {
            "Overview": "/static/audio/ips/overview.mp3",
            "Benefits": "/static/audio/ips/benefits.mp3",
            "Impact": "/static/audio/ips/impact.mp3",
            "InitialChoice": "/static/audio/ips/initial_choice.mp3",
            "Scenario1": "/static/audio/ips/scenario1.mp3",
            "Scenario2": "/static/audio/ips/cenario2.mp3",
            "Result": "/static/audio/ips/result.mp3"
        },
        "InitialChoice": {
            "Question": "What defines your policing approach?",
            "Options": [
                {
                    "type": "Personal",
                    "text": "Build elite investigation capabilities and modern policing systems",
                    "briefing": "You'll revolutionize crime-solving through forensic excellence and data-driven policing models."
                },
                {
                    "type": "Community",
                    "text": "Implement community policing and build public trust through engagement",
                    "briefing": "You'll prevent crimes through grassroots intelligence and collaborative safety partnerships."
                }
            ]
        },
        "Scenarios": [
            {
                "Level": 1,
                "Title": "Communal Violence Eruption",
                "Description": "Religious tensions erupt into violent clashes during a festival procession. Mobs are destroying properties with casualties rising by the minute.",
                "DecisionCards": [
                    {
                        "Option": "Lead riot control personally with maximum restraint and precision",
                        "Outcomes": {"PersonalImpact": 8, "CommunityImpact": 7},
                        "Feedback": "Your courageous leadership prevented escalation and saved countless lives through measured response."
                    },
                    {
                        "Option": "Contain perimeter while negotiating with community leaders",
                        "Outcomes": {"PersonalImpact": 2, "CommunityImpact": 5},
                        "Feedback": "While negotiation is vital, delayed intervention allowed violence to spread in critical zones."
                    }
                ]
            },
            {
                "Level": 2,
                "Title": "High-Profile Corruption Case",
                "Description": "Evidence implicates powerful politicians in organized crime. Your superiors suggest 'pragmatism' while media pressures for action.",
                "DecisionCards": [
                    {
                        "Option": "Build airtight case with digital evidence and constitutional safeguards",
                        "Outcomes": {"PersonalImpact": 9, "CommunityImpact": 8},
                        "Feedback": "Your meticulous due process secured historic convictions while strengthening institutional integrity."
                    },
                    {
                        "Option": "Transfer case to central agencies to avoid direct confrontation",
                        "Outcomes": {"PersonalImpact": -3, "CommunityImpact": -4},
                        "Feedback": "Avoiding responsibility damaged police credibility and emboldened criminal-political nexus."
                    }
                ]
            }
        ],
        "Verdicts": {
            "high": "You've been the shield of justice, combining courage with compassion. Your leadership redefined policing standards and inspired a generation.",
            "medium": "A dependable officer who maintained order. Greater boldness against power structures could have created transformative change.",
            "low": "Policing challenges revealed growth areas. Remember that true authority comes from moral courage, not just rank."
        }
    },
    "Teacher": {
        "CareerCard": {
            "Title": "Teacher",
            "Stream": "Education",
            "AvatarMale": "/static/images/teacher_avatar_male.png",
            "AvatarFemale": "/static/images/teacher_avatar_female.png",
            "Overview": "As an educator, you'll shape young minds, ignite curiosity, and build foundational knowledge while adapting to diverse learning needs in evolving educational landscapes.",
            "BenefitsAndChallenges": {
                "Benefits": [
                    "Profound impact on future generations",
                    "Creative fulfillment through pedagogy innovation",
                    "Continuous learning from student interactions"
                ],
                "JobChallenges": [
                    "Managing diverse learning needs in large classrooms",
                    "Administrative burdens reducing teaching time",
                    "Limited resources for optimal educational experiences"
                ]
            },
            "DualImpactHighlights": {
                "PersonalGrowth": "Develops exceptional communication, empathy, and creative problem-solving through daily educational challenges.",
                "CommunityImpact": "Builds society's foundation by equipping youth with knowledge, critical thinking, and civic values."
            }
        },
        "Images": { 
            "Overview": "/static/images/teacher/overview.png",
            "Benefits": "/static/images/teacher/benefits.png",
            "Impact": "/static/images/teacher/impact.png",
            "InitialChoice": "/static/images/teacher/choice.png",
            "Scenario1": "/static/images/teacher/scenario1.png",
            "Scenario2": "/static/images/teacher/scenario2.png",
            "Result": "/static/images/teacher/result.png"
        },
        "Audio": {
            "Overview": "/static/audio/teacher/overview.mp3",
            "Benefits": "/static/audio/teacher/benefits.mp3",
            "Impact": "/static/audio/teacher/impact.mp3",
            "InitialChoice": "/static/audio/teacher/initial_choice.mp3",
            "Scenario1": "/static/audio/teacher/scenario1.mp3",
            "Scenario2": "/static/audio/teacher/scenario2.mp3",
            "Result": "/static/audio/teacher/result.mp3"
        },
        "InitialChoice": {
            "Question": "What's your core teaching philosophy?",
            "Options": [
                {
                    "type": "Personal",
                    "text": "Master subject expertise to inspire academic excellence",
                    "briefing": "You'll create deep content mastery through innovative pedagogy and rigorous intellectual standards."
                },
                {
                    "type": "Community",
                    "text": "Focus on holistic development and inclusive learning environments",
                    "briefing": "You'll nurture well-rounded individuals through socio-emotional learning and community classrooms."
                }
            ]
        },
        "Scenarios": [
            {
                "Level": 1,
                "Title": "Digital Divide Challenge",
                "Description": "During hybrid learning, underprivileged students disengage due to limited tech access. Performance gaps widen dramatically.",
                "DecisionCards": [
                    {
                        "Option": "Develop offline learning kits and peer-sharing systems",
                        "Outcomes": {"PersonalImpact": 6, "CommunityImpact": 8},
                        "Feedback": "Your inclusive approach brought every student back into the learning community through creative solutions."
                    },
                    {
                        "Option": "Focus on digital upskilling for tech-enabled students",
                        "Outcomes": {"PersonalImpact": 4, "CommunityImpact": 2},
                        "Feedback": "While tech-forward students thrived, equity gaps widened creating classroom divisions."
                    }
                ]
            },
            {
                "Level": 2,
                "Title": "Curriculum Transformation",
                "Description": "Your school resists updating outdated curriculum. Students disengage while parents demand exam-focused traditional teaching.",
                "DecisionCards": [
                    {
                        "Option": "Pilot innovative modules showing improved outcomes through evidence",
                        "Outcomes": {"PersonalImpact": 7, "CommunityImpact": 7},
                        "Feedback": "Your evidence-based approach gradually transformed pedagogy while winning stakeholder trust."
                    },
                    {
                        "Option": "Comply with existing systems while supplementing privately",
                        "Outcomes": {"PersonalImpact": -2, "CommunityImpact": -3},
                        "Feedback": "Maintaining status quo perpetuated irrelevant education, failing student futures."
                    }
                ]
            }
        ],
        "Verdicts": {
            "high": "You've lit countless lamps of knowledge. Your students carry forward not just lessons, but transformed ways of thinking that will better our world.",
            "medium": "A dedicated educator who shaped many young minds. Greater innovation could have multiplied your impact beyond the classroom.",
            "low": "Teaching revealed undiscovered strengths. Remember that education's power lies in believing in unseen potential - in students and yourself."
        }
    },
    "Cybersecurity Analyst": {
        "CareerCard": {
            "Title": "Cybersecurity Analyst",
            "Stream": "Technology",
            "AvatarMale": "/static/images/cyber_avatar_male.png",
            "AvatarFemale": "/static/images/cyber_avatar_female.png",
            "Overview": "As a digital guardian, you'll protect critical systems from cyber threats, conduct vulnerability assessments, and develop security protocols in an evolving threat landscape.",
            "BenefitsAndChallenges": {
                "Benefits": [
                    "High demand with competitive compensation",
                    "Intellectual challenge in constantly evolving field",
                    "Critical role in national/economic security"
                ],
                "JobChallenges": [
                    "High-pressure incident response scenarios",
                    "Staying ahead of sophisticated threat actors",
                    "Balancing security with usability requirements"
                ]
            },
            "DualImpactHighlights": {
                "PersonalGrowth": "Develops cutting-edge technical expertise, forensic investigation skills, and strategic risk assessment capabilities.",
                "CommunityImpact": "Safeguards digital infrastructure, protects citizen data, and enables secure digital transformation."
            }
        },
        "Images": { 
            "Overview": "/static/images/cybersecurity/overview.png",
            "Benefits": "/static/images/cybersecurity/benefits.png",
            "Impact": "/static/images/cybersecurity/impact.png",
            "InitialChoice": "/static/images/cybersecurity/choice.png",
            "Scenario1": "/static/images/cybersecurity/scenario1.png",
            "Scenario2": "/static/images/cybersecurity/scenario2.png",
            "Result": "/static/images/cybersecurity/result.png"
        },
        "Audio": {
            "Overview": "/static/audio/cybersecurity/overview.mp3",
            "Benefits": "/static/audio/cybersecurity/benefits.mp3",
            "Impact": "/static/audio/cybersecurity/impact.mp3",
            "InitialChoice": "/static/audio/cybersecurity/initial_choice.mp3",
            "Scenario1": "/static/audio/cybersecurity/scenario1.mp3",
            "Scenario2": "/static/audio/cybersecurity/scenario2.mp3",
            "Result": "/static/audio/cybersecurity/result.mp3"
        },
        "InitialChoice": {
            "Question": "How do you approach digital defense?",
            "Options": [
                {
                    "type": "Personal",
                    "text": "Master offensive security to anticipate attacker methodologies",
                    "briefing": "You'll develop elite penetration testing and threat hunting capabilities through adversarial mindset."
                },
                {
                    "type": "Community",
                    "text": "Build resilient systems through architecture security and awareness",
                    "briefing": "You'll create security-by-design frameworks and organizational culture to reduce vulnerabilities."
                }
            ]
        },
        "Scenarios": [
            {
                "Level": 1,
                "Title": "Ransomware Attack",
                "Description": "Critical hospital systems are encrypted by ransomware. Attackers demand cryptocurrency while emergency services are disrupted.",
                "DecisionCards": [
                    {
                        "Option": "Lead incident response: isolate networks, deploy backups, trace attack vectors",
                        "Outcomes": {"PersonalImpact": 8, "CommunityImpact": 9},
                        "Feedback": "Your rapid containment saved lives by restoring critical systems while preserving forensic evidence."
                    },
                    {
                        "Option": "Negotiate with attackers to buy restoration time",
                        "Outcomes": {"PersonalImpact": -5, "CommunityImpact": -7},
                        "Feedback": "Delaying containment allowed malware to spread, causing greater damage and encouraging future attacks."
                    }
                ]
            },
            {
                "Level": 2,
                "Title": "Zero-Day Vulnerability",
                "Description": "You discover a critical flaw in widely used software. Disclosing it could prevent disasters but might be weaponized before patches deploy.",
                "DecisionCards": [
                    {
                        "Option": "Coordinate responsible disclosure through CERT channels",
                        "Outcomes": {"PersonalImpact": 7, "CommunityImpact": 8},
                        "Feedback": "Your ethical approach enabled global patching, preventing mass exploitation while establishing trust."
                    },
                    {
                        "Option": "Sell vulnerability to highest bidder for defensive research",
                        "Outcomes": {"PersonalImpact": -8, "CommunityImpact": -9},
                        "Feedback": "Prioritizing profit over ethics potentially armed malicious actors, causing global harm."
                    }
                ]
            }
        ],
        "Verdicts": {
            "high": "You've been the invisible shield of our digital age. Your vigilance prevented catastrophes while your ethical leadership raised industry standards.",
            "medium": "A skilled analyst who secured critical systems. Broader security architecture thinking could have created systemic resilience.",
            "low": "Cybersecurity challenges revealed gaps. Remember that true security stems from integrity as much as technical skill."
        }
    },
    "Data Analyst": {
        "CareerCard": {
            "Title": "Data Analyst",
            "Stream": "Technology",
            "AvatarMale": "/static/images/data_avatar_male.png",
            "AvatarFemale": "/static/images/data_avatar_female.png",
            "Overview": "As an insights architect, you'll transform raw data into actionable intelligence through statistical analysis, visualization, and strategic interpretation across domains.",
            "BenefitsAndChallenges": {
                "Benefits": [
                    "High demand across industries with competitive pay",
                    "Intellectual satisfaction solving complex puzzles",
                    "Tangible impact on strategic decisions"
                ],
                "JobChallenges": [
                    "Cleaning/organizing imperfect real-world data",
                    "Communicating technical insights to non-technical stakeholders",
                    "Avoiding bias in data interpretation"
                ]
            },
            "DualImpactHighlights": {
                "PersonalGrowth": "Develops advanced analytical reasoning, statistical modeling expertise, and cross-functional communication skills.",
                "CommunityImpact": "Drives evidence-based decision making, optimizes resource allocation, and reveals systemic opportunities."
            }
        },
        "Images": { 
            "Overview": "/static/images/data/overview.png",
            "Benefits": "/static/images/data/benefits.png",
            "Impact": "/static/images/data/impact.png",
            "InitialChoice": "/static/images/data/choice.png",
            "Scenario1": "/static/images/data/scenario1.png",
            "Scenario2": "/static/images/data/scenario2.png",
            "Result": "/static/images/data/result.png"
        },
        "Audio": {
            "Overview": "/static/audio/data/overview.mp3",
            "Benefits": "/static/audio/data/benefits.mp3",
            "Impact": "/static/audio/data/impact.mp3",
            "InitialChoice": "/static/audio/data/initial_choice.mp3",
            "Scenario1": "/static/audio/data/scenario1.mp3",
            "Scenario2": "/static/audio/data/scenario2.mp3",
            "Result": "/static/audio/data/result.mp3"
        },
        "InitialChoice": {
            "Question": "How do you derive meaning from data?",
            "Options": [
                {
                    "type": "Personal",
                    "text": "Master advanced analytics and machine learning techniques",
                    "briefing": "You'll develop cutting-edge predictive modeling capabilities through technical excellence."
                },
                {
                    "type": "Community",
                    "text": "Focus on actionable insights and stakeholder communication",
                    "briefing": "You'll transform data into strategic narratives that drive organizational decisions."
                }
            ]
        },
        "Scenarios": [
            {
                "Level": 1,
                "Title": "Healthcare Disparity Analysis",
                "Description": "Your hospital data reveals alarming treatment outcome gaps across demographics. Leadership wants quick fixes while frontline staff resist scrutiny.",
                "DecisionCards": [
                    {
                        "Option": "Conduct root-cause analysis and co-create solutions with affected communities",
                        "Outcomes": {"PersonalImpact": 7, "CommunityImpact": 9},
                        "Feedback": "Your inclusive approach developed sustainable solutions while building organizational trust."
                    },
                    {
                        "Option": "Optimize statistical models for publication in medical journals",
                        "Outcomes": {"PersonalImpact": 6, "CommunityImpact": 3},
                        "Feedback": "While academically rigorous, your approach failed to translate insights into practical improvements."
                    }
                ]
            },
            {
                "Level": 2,
                "Title": "Ethical Data Dilemma",
                "Description": "Marketing wants to monetize user behavior data in ways that violate privacy principles. Pressure mounts to 'find legal justifications'.",
                "DecisionCards": [
                    {
                        "Option": "Develop ethical framework with anonymization and explicit consent mechanisms",
                        "Outcomes": {"PersonalImpact": 8, "CommunityImpact": 7},
                        "Feedback": "You balanced innovation with ethics, building long-term customer trust through transparency."
                    },
                    {
                        "Option": "Maximize short-term revenue through aggressive data utilization",
                        "Outcomes": {"PersonalImpact": -6, "CommunityImpact": -8},
                        "Feedback": "Prioritizing profit over privacy triggered regulatory penalties and brand erosion."
                    }
                ]
            }
        ],
        "Verdicts": {
            "high": "You transformed numbers into narratives that changed organizations. Your insights created value while your ethics protected vulnerable communities.",
            "medium": "A skilled analyst who delivered valuable reports. Greater strategic influence could have turned insights into systemic transformation.",
            "low": "Data revealed patterns in your own growth journey. Remember that numbers measure what we value, but values determine what we measure."
        }
    },
    "AI Engineer": {
        "CareerCard": {
            "Title": "AI Engineer",
            "Stream": "Technology",
            "AvatarMale": "/static/images/ai_avatar_male.png",
            "AvatarFemale": "/static/images/ai_avatar_female.png",
            "Overview": "As an artificial intelligence architect, you'll design, build, and deploy intelligent systems that learn from data to automate decisions and augment human capabilities.",
            "BenefitsAndChallenges": {
                "Benefits": [
                    "Pioneer transformative technologies",
                    "Solve complex problems at scale",
                    "High compensation and rapid career growth"
                ],
                "JobChallenges": [
                    "Managing ethical implications of autonomous systems",
                    "Explaining complex models to stakeholders",
                    "Keeping pace with exponential technological change"
                ]
            },
            "DualImpactHighlights": {
                "PersonalGrowth": "Develops cutting-edge technical skills in machine learning, system architecture, and algorithmic problem-solving.",
                "CommunityImpact": "Creates intelligent solutions for global challenges while shaping ethical AI adoption across society."
            }
        },
        "Images": { 
            "Overview": "/static/images/ai/overview.png",
            "Benefits": "/static/images/ai/benefits.png",
            "Impact": "/static/images/ai/impact.png",
            "InitialChoice": "/static/images/ai/choice.png",
            "Scenario1": "/static/images/ai/scenario1.png",
            "Scenario2": "/static/images/ai/scenario2.png",
            "Result": "/static/images/ai/result.png"
        },
        "Audio": {
            "Overview": "/static/audio/ai/overview.mp3",
            "Benefits": "/static/audio/ai/benefits.mp3",
            "Impact": "/static/audio/ai/impact.mp3",
            "InitialChoice": "/static/audio/ai/initial_choice.mp3",
            "Scenario1": "/static/audio/ai/scenario1.mp3",
            "Scenario2": "/static/audio/ai/scenario2.mp3",
            "Result": "/static/audio/ai/result.mp3"
        },
        "InitialChoice": {
            "Question": "How will you shape AI development?",
            "Options": [
                {
                    "type": "Personal",
                    "text": "Push boundaries of AI capabilities through research breakthroughs",
                    "briefing": "You'll advance state-of-the-art algorithms and model architectures through technical innovation."
                },
                {
                    "type": "Community",
                    "text": "Develop accessible AI tools solving real-world problems",
                    "briefing": "You'll democratize AI benefits through user-centric applications addressing societal needs."
                }
            ]
        },
        "Scenarios": [
            {
                "Level": 1,
                "Title": "Algorithmic Bias Discovery",
                "Description": "Your hiring algorithm shows gender bias against female candidates. Leadership pressures for quick deployment despite ethical concerns.",
                "DecisionCards": [
                    {
                        "Option": "Rebuild with fairness constraints and bias auditing protocols",
                        "Outcomes": {"PersonalImpact": 6, "CommunityImpact": 8},
                        "Feedback": "Your principled approach created equitable AI while establishing ethical standards."
                    },
                    {
                        "Option": "Deploy with minor adjustments to meet deadlines",
                        "Outcomes": {"PersonalImpact": -4, "CommunityImpact": -7},
                        "Feedback": "Biased implementation caused discrimination lawsuits and reputational damage."
                    }
                ]
            },
            {
                "Level": 2,
                "Title": "Autonomous Weapons Dilemma",
                "Description": "Military contractors want your target recognition system for lethal drones. Colleagues argue it could save soldiers' lives.",
                "DecisionCards": [
                    {
                        "Option": "Develop civilian applications enhancing disaster response capabilities",
                        "Outcomes": {"PersonalImpact": 9, "CommunityImpact": 8},
                        "Feedback": "You redirected technology toward life-saving applications, establishing ethical leadership."
                    },
                    {
                        "Option": "Proceed with military contract under 'government oversight'",
                        "Outcomes": {"PersonalImpact": -9, "CommunityImpact": -10},
                        "Feedback": "Your technology enabled autonomous killing, triggering global arms race concerns."
                    }
                ]
            }
        ],
        "Verdicts": {
            "high": "You engineered intelligence with wisdom. Your innovations solved human problems while your ethical frameworks protected society from unintended consequences.",
            "medium": "A skilled developer who built powerful systems. Stronger ethical safeguards could have amplified positive impact.",
            "low": "AI development revealed complex tradeoffs. Remember that technology magnifies human intent - ensure yours creates light, not shadows."
        }
    },
    "UX Engineer": {
        "CareerCard": {
            "Title": "UX Engineer",
            "Stream": "Technology",
            "AvatarMale": "/static/images/ux_avatar_male.png",
            "AvatarFemale": "/static/images/ux_avatar_female.png",
            "Overview": "As a user experience architect, you'll bridge design and engineering to create intuitive, accessible digital products through prototyping, testing, and iterative refinement.",
            "BenefitsAndChallenges": {
                "Benefits": [
                    "Tangible impact on user satisfaction",
                    "Creative-technical hybrid role",
                    "High demand across industries"
                ],
                "JobChallenges": [
                    "Balancing user needs with business constraints",
                    "Quantifying subjective experience improvements",
                    "Staying current with evolving interaction paradigms"
                ]
            },
            "DualImpactHighlights": {
                "PersonalGrowth": "Develops empathy-driven design thinking, technical prototyping skills, and cross-functional collaboration abilities.",
                "CommunityImpact": "Makes technology accessible and empowering for diverse populations while reducing digital exclusion."
            }
        },
        "Images": { 
            "Overview": "/static/images/ux/overview.png",
            "Benefits": "/static/images/ux/benefits.png",
            "Impact": "/static/images/ux//ux/impact.png",
            "InitialChoice": "/static/images/ux/choice.png",
            "Scenario1": "/static/images/ux/scenario1.png",
            "Scenario2": "/static/images/ux/scenario2.png",
            "Result": "/static/images/ux/result.png"
        },
        "Audio": {
            "Overview": "/static/audio/ux/overview.mp3",
            "Benefits": "/static/audio/ux/benefits.mp3",
            "Impact": "/static/audio/ux/impact.mp3",
            "InitialChoice": "/static/audio/ux/initial_choice.mp3",
            "Scenario1": "/static/audio/ux/scenario1.mp3",
            "Scenario2": "/static/audio/ux/scenario2.mp3",
            "Result": "/static/audio/ux/result.mp3"
        },
        "InitialChoice": {
            "Question": "What drives your design philosophy?",
            "Options": [
                {
                    "type": "Personal",
                    "text": "Pioneer innovative interaction paradigms through technical prototyping",
                    "briefing": "You'll create breakthrough experiences by pushing boundaries of interface technology."
                },
                {
                    "type": "Community",
                    "text": "Champion inclusive design for underrepresented populations",
                    "briefing": "You'll ensure technology serves diverse needs through accessibility-first approaches."
                }
            ]
        },
        "Scenarios": [
            {
                "Level": 1,
                "Title": "Accessibility Overhaul",
                "Description": "User testing reveals your banking app excludes visually impaired customers. Management resists costly redesign for 'small user segment'.",
                "DecisionCards": [
                    {
                        "Option": "Build business case showing legal/compliance benefits while implementing WCAG standards",
                        "Outcomes": {"PersonalImpact": 7, "CommunityImpact": 8},
                        "Feedback": "Your advocacy made finance accessible to thousands while preventing discrimination lawsuits."
                    },
                    {
                        "Option": "Add basic screen reader support as minimum compliance",
                        "Outcomes": {"PersonalImpact": 3, "CommunityImpact": 2},
                        "Feedback": "Partial solution failed to address core accessibility barriers, perpetuating exclusion."
                    }
                ]
            },
            {
                "Level": 2,
                "Title": "Dark Pattern Dilemma",
                "Description": "Product leadership insists on manipulative designs to boost metrics. Data shows they work but violate ethical guidelines.",
                "DecisionCards": [
                    {
                        "Option": "Prove ethical alternatives achieving business goals through genuine value",
                        "Outcomes": {"PersonalImpact": 8, "CommunityImpact": 7},
                        "Feedback": "Your solutions balanced business needs with user respect, building sustainable trust."
                    },
                    {
                        "Option": "Implement subtle dark patterns disguised as 'growth hacks'",
                        "Outcomes": {"PersonalImpact": -6, "CommunityImpact": -8},
                        "Feedback": "Short-term metrics came at cost of user trust and eventual regulatory penalties."
                    }
                ]
            }
        ],
        "Verdicts": {
            "high": "You humanized technology with every interaction. Your designs empowered diverse populations while setting new standards for digital ethics.",
            "medium": "A talented designer who created functional interfaces. Deeper user advocacy could have transformed exclusionary systems.",
            "low": "Design challenges revealed new dimensions. Remember that true UX begins with seeing humans, not just users."
        }
    },
    "Software Engineer": {
        "CareerCard": {
            "Title": "Software Engineer",
            "Stream": "Technology",
            "AvatarMale": "/static/images/sw_avatar_male.png",
            "AvatarFemale": "/static/images/sw_avatar_female.png",
            "Overview": "As a digital architect, you'll design, build, and maintain software systems that power modern life - from applications to infrastructure - while balancing technical constraints.",
            "BenefitsAndChallenges": {
                "Benefits": [
                    "Creative power to build solutions from abstract concepts",
                    "High demand with global opportunities",
                    "Continuous learning in evolving tech landscape"
                ],
                "JobChallenges": [
                    "Managing technical debt in complex systems",
                    "Translating ambiguous requirements into technical specifications",
                    "Balancing perfectionism with delivery timelines"
                ]
            },
            "DualImpactHighlights": {
                "PersonalGrowth": "Develops abstract problem-solving, systems thinking, and collaborative creation skills through complex projects.",
                "CommunityImpact": "Builds digital infrastructure enabling innovation across industries while creating tools that transform lives."
            }
        },
        "Images": { 
            "Overview": "/static/images/se/overview.png",
            "Benefits": "/static/images/se/benefits.png",
            "Impact": "/static/images/se/impact.png",
            "InitialChoice": "/static/images/se/choice.png",
            "Scenario1": "/static/images/se/scenario1.png",
            "Scenario2": "/static/images/se/scenario2.png",
            "Result": "/static/images/se/result.png"
        },
        "Audio": {
            "Overview": "/static/audio/se/overview.mp3",
            "Benefits": "/static/audio/se/benefits.mp3",
            "Impact": "/static/audio/se/impact.mp3",
            "InitialChoice": "/static/audio/se/initial_choice.mp3",
            "Scenario1": "/static/audio/se/scenario1.mp3",
            "Scenario2": "/static/audio/se/scenario2.mp3",
            "Result": "/static/audio/se/result.mp3"
        },
        "InitialChoice": {
            "Question": "What's your engineering ethos?",
            "Options": [
                {
                    "type": "Personal",
                    "text": "Master cutting-edge technologies and architectural excellence",
                    "briefing": "You'll build robust, scalable systems through technical mastery and engineering rigor."
                },
                {
                    "type": "Community",
                    "text": "Develop solutions addressing social/environmental challenges",
                    "briefing": "You'll leverage technology for public good through mission-driven engineering."
                }
            ]
        },
        "Scenarios": [
            {
                "Level": 1,
                "Title": "Technical Debt Crisis",
                "Description": "Rushed features created unstable legacy code. Management demands new functionality while system failures increase.",
                "DecisionCards": [
                    {
                        "Option": "Implement refactoring sprints with automated testing while educating stakeholders",
                        "Outcomes": {"PersonalImpact": 7, "CommunityImpact": 6},
                        "Feedback": "Your technical leadership improved system health while aligning business on sustainable practices."
                    },
                    {
                        "Option": "Patch immediate issues while building new features",
                        "Outcomes": {"PersonalImpact": -3, "CommunityImpact": -4},
                        "Feedback": "Accumulating technical debt eventually caused catastrophic system failures."
                    }
                ]
            },
            {
                "Level": 2,
                "Title": "Surveillance Feature Demand",
                "Description": "Government requests backdoor access to your communication platform for 'national security'. Refusal could ban your service in key markets.",
                "DecisionCards": [
                    {
                        "Option": "Develop end-to-end encryption while fighting for digital rights",
                        "Outcomes": {"PersonalImpact": 8, "CommunityImpact": 9},
                        "Feedback": "You protected user privacy while setting industry standards for digital security."
                    },
                    {
                        "Option": "Comply quietly with minimal implementation",
                        "Outcomes": {"PersonalImpact": -7, "CommunityImpact": -8},
                        "Feedback": "Your compromise enabled authoritarian surveillance, betraying user trust."
                    }
                ]
            }
        ],
        "Verdicts": {
            "high": "You built more than code - you engineered foundations for progress. Your systems empowered millions while your ethics protected fundamental rights.",
            "medium": "A competent engineer who delivered functional systems. Greater architectural vision could have created transformative platforms.",
            "low": "Coding challenges revealed debugging opportunities. Remember that elegant solutions emerge from understanding deeper patterns, not just fixing surface errors."
        }
    },
    "Web Developer": {
        "CareerCard": {
            "Title": "Web Developer",
            "Stream": "Technology",
            "AvatarMale": "/static/images/web_avatar_male.png",
            "AvatarFemale": "/static/images/web_avatar_female.png",
            "Overview": "As an internet architect, you'll create and maintain websites/web applications that connect people, information, and services across the digital ecosystem.",
            "BenefitsAndChallenges": {
                "Benefits": [
                    "Tangible creative output with visible impact",
                    "Diverse industry applications",
                    "Remote work flexibility"
                ],
                "JobChallenges": [
                    "Managing compatibility across browsers/devices",
                    "Security vulnerabilities in client-facing systems",
                    "Keeping pace with evolving frameworks/tools"
                ]
            },
            "DualImpactHighlights": {
                "PersonalGrowth": "Develops full-stack technical skills, creative problem-solving, and client communication abilities.",
                "CommunityImpact": "Builds digital public spaces that democratize information access and enable global connections."
            }
        },
        "Images": { 
            "Overview": "/static/images/web/overview.png",
            "Benefits": "/static/images/web/benefits.png",
            "Impact": "/static/images/web/impact.png",
            "InitialChoice": "/static/images/web/choice.png",
            "Scenario1": "/static/images/web/scenario1.png",
            "Scenario2": "/static/images/web/scenario2.png",
            "Result": "/static/images/web/result.png"
        },
        "Audio": {
            "Overview": "/static/audio/web/overview.mp3",
            "Benefits": "/static/audio/web/benefits.mp3",
            "Impact": "/static/audio/web/impact.mp3",
            "InitialChoice": "/static/audio/web/initial_choice.mp3",
            "Scenario1": "/static/audio/web/scenario1.mp3",
            "Scenario2": "/static/audio/web/scenario2.mp3",
            "Result": "/static/audio/web/result.mp3"
        },
        "InitialChoice": {
            "Question": "How do you approach web creation?",
            "Options": [
                {
                    "type": "Personal",
                    "text": "Master advanced frameworks and cutting-edge interactive experiences",
                    "briefing": "You'll create technically sophisticated web applications pushing performance boundaries."
                },
                {
                    "type": "Community",
                    "text": "Develop accessible, performant websites for underserved communities",
                    "briefing": "You'll bridge digital divides through inclusive design and lightweight solutions."
                }
            ]
        },
        "Scenarios": [
            {
                "Level": 1,
                "Title": "Small Business Rescue",
                "Description": "Traditional shops need e-commerce survival during pandemic lockdowns. They lack digital literacy and have minimal budgets.",
                "DecisionCards": [
                    {
                        "Option": "Develop simplified CMS with training for sustainable self-management",
                        "Outcomes": {"PersonalImpact": 6, "CommunityImpact": 9},
                        "Feedback": "Your empowering approach helped dozens of businesses survive while building digital capabilities."
                    },
                    {
                        "Option": "Build custom solutions requiring ongoing paid maintenance",
                        "Outcomes": {"PersonalImpact": 5, "CommunityImpact": 3},
                        "Feedback": "While technically sound, your solution created dependency rather than empowerment."
                    }
                ]
            },
            {
                "Level": 2,
                "Title": "Addiction Mechanics Demand",
                "Description": "Client insists on engagement-maximizing features that exploit psychological vulnerabilities. Data shows significant revenue potential.",
                "DecisionCards": [
                    {
                        "Option": "Implement ethical alternatives using positive reinforcement and wellbeing metrics",
                        "Outcomes": {"PersonalImpact": 7, "CommunityImpact": 8},
                        "Feedback": "You proved ethical design can be profitable while protecting user wellbeing."
                    },
                    {
                        "Option": "Deploy demanded features with minimal friction points",
                        "Outcomes": {"PersonalImpact": -5, "CommunityImpact": -7},
                        "Feedback": "Your designs contributed to digital addiction epidemics, harming vulnerable users."
                    }
                ]
            }
        ],
        "Verdicts": {
            "high": "You built bridges across the digital divide. Your websites became community assets while your ethical standards made the web more human.",
            "medium": "A skilled developer who created functional sites. Greater accessibility focus could have expanded your impact exponentially.",
            "low": "Web challenges revealed debugging opportunities. Remember that the most elegant code serves human needs, not just technical specs."
        }
    },
    "Nurse": {
        "CareerCard": {
            "Title": "Nurse",
            "Stream": "Healthcare",
            "AvatarMale": "/static/images/nurse_avatar_male.png",
            "AvatarFemale": "/static/images/nurse_avatar_female.png",
            "Overview": "As a nursing professional, you'll provide critical patient care, coordinate treatment plans, and offer compassionate support during vulnerable health journeys.",
            "BenefitsAndChallenges": {
                "Benefits": [
                    "Deep human connection through caregiving",
                    "Diverse specializations and work environments",
                    "Strong job security with shift flexibility"
                ],
                "JobChallenges": [
                    "Emotional toll of patient suffering",
                    "Physically demanding long shifts",
                    "Balancing clinical efficiency with compassionate care"
                ]
            },
            "DualImpactHighlights": {
                "PersonalGrowth": "Develops exceptional empathy, crisis management, and interdisciplinary collaboration skills.",
                "CommunityImpact": "Serves as frontline healthcare guardian, improving patient outcomes and promoting public health."
            }
        },
        "Images": { 
            "Overview": "/static/images/nurse/overview.png",
            "Benefits": "/static/images/nurse/benefits.png",
            "Impact": "/static/images/nurse/impact.png",
            "InitialChoice": "/static/images/nurse/choice.png",
            "Scenario1": "/static/images/nurse/scenario1.png",
            "Scenario2": "/static/images/nurse/scenario2.png",
            "Result": "/static/images/nurse/result.png"
        },
        "Audio": {
            "Overview": "/static/audio/nurse/overview.mp3",
            "Benefits": "/static/audio/nurse/benefits.mp3",
            "Impact": "/static/audio/nurse/impact.mp3",
            "InitialChoice": "/static/audio/nurse/initial_choice.mp3",
            "Scenario1": "/static/audio/nurse/scenario1.mp3",
            "Scenario2": "/static/audio/nurse/scenario2.mp3",
            "Result": "/static/audio/nurse/result.mp3"
        },
        "InitialChoice": {
            "Question": "What defines your nursing approach?",
            "Options": [
                {
                    "type": "Personal",
                    "text": "Specialize in critical care and advanced clinical skills",
                    "briefing": "You'll develop expert capabilities to handle complex medical emergencies."
                },
                {
                    "type": "Community",
                    "text": "Focus on preventive care and community health education",
                    "briefing": "You'll empower populations through health literacy and accessible preventive services."
                }
            ]
        },
        "Scenarios": [
            {
                "Level": 1,
                "Title": "End-of-Life Dilemma",
                "Description": "A terminal patient requests dignified cessation of painful treatments. Family insists on aggressive interventions against medical advice.",
                "DecisionCards": [
                    {
                        "Option": "Facilitate family conference with palliative specialists to find consensus",
                        "Outcomes": {"PersonalImpact": 8, "CommunityImpact": 7},
                        "Feedback": "Your compassionate mediation honored patient autonomy while supporting grieving families."
                    },
                    {
                        "Option": "Follow family demands to avoid conflict",
                        "Outcomes": {"PersonalImpact": -4, "CommunityImpact": -5},
                        "Feedback": "Avoiding difficult conversations resulted in unnecessary patient suffering."
                    }
                ]
            },
            {
                "Level": 2,
                "Title": "Vaccine Hesitancy Crisis",
                "Description": "Community resists lifesaving vaccines due to misinformation. Local leaders undermine public health efforts.",
                "DecisionCards": [
                    {
                        "Option": "Organize community dialogues with trusted figures and recovered patients",
                        "Outcomes": {"PersonalImpact": 6, "CommunityImpact": 9},
                        "Feedback": "Your grassroots approach built vaccine acceptance through empathy and evidence."
                    },
                    {
                        "Option": "Focus strictly on clinical duties avoiding community engagement",
                        "Outcomes": {"PersonalImpact": 2, "CommunityImpact": -3},
                        "Feedback": "Avoiding community leadership allowed preventable diseases to resurge."
                    }
                ]
            }
        ],
        "Verdicts": {
            "high": "You were the healing hand and comforting voice when it mattered most. Your clinical excellence and compassion transformed countless health journeys.",
            "medium": "A dedicated nurse who provided competent care. Greater advocacy could have improved systemic healthcare delivery.",
            "low": "Nursing challenges revealed untapped strength. Remember that healing combines technical skill with human connection."
        }
    }
}