// matcher.js
function matchResume(resumeData, jobData) {
    if (!resumeData || !resumeData.text || !jobData) return { score: 0, feedback: [] };
  
    const resumeText = resumeData.text.toLowerCase();
    let score = 0;
    const feedback = [];
  
    // Match technical skills
    if (jobData.skills) {
      jobData.skills.forEach(skill => {
        if (resumeText.includes(skill.toLowerCase())) {
          score += 10;
        } else {
          feedback.push(`Missing skill: ${skill}`);
        }
      });
    }
  
    // Match experience
    if (jobData.experience) {
      score += Math.min((parseInt(resumeData.experienceYears) || 0), jobData.experience) * 5;
    }
  
    return { score, feedback };
  }
  
  module.exports = { matchResume };