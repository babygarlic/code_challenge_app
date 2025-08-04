import "react"
import { useState, useEffect } from "react"
import { MCQChallenge } from "./MCQChallenge"

export function ChallengeGenerator() {
    const [challenge, setChallenge] = useState(null)
    const [isloading, setIsLoading] = useState(false)
    const [error, setError] = useState(null)
    const [difficulty, setDifficulty] = useState("easy")
    const [quota,setQuota] = useState(null)

    const fetchQuota = async () => {}

    const generateChallenge = async () => {}
    const getNextResetTime = () => {}


    return <div className="challenge-container">
        <h2>Coding challenge generator</h2>
        <div className="qouta-display">
            <p>Challenge remaining today: {quota?.quota_remaining||0}</p>
            {quota?.quota_remaining === 0 && (
                <p>Next reset time: {0}</p>
            )}
        </div>
        <div className="difficulty-selector">
            <label htmlFor="difficulty">Select Difficulty</label>
            <select 
                id="difficulty" 
                value={difficulty} 
                onChange={(e) => setDifficulty(e.target.value)}
                disabled={isloading}
            >
                <option value="easy">Easy</option>
                <option value="medium">Medium</option>
                <option value="hard">Hard</option>
            </select>
        </div>
        <button 
            onClick={generateChallenge} 
            disabled={isloading || quota?.quota_remaining === 0}
            className="generate-button"
            >
                {isloading ? "Generating..." : "Generate Challenge"}
        </button>
        {error && <div className="error-message">
                        <p>{error}</p>
        </div>}

        {challenge && <MCQChallenge challenge={challenge}/>}
        
    </div>  
}
