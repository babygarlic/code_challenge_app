import 'react'
import {useState, useEffect} from 'react'
import {MCQChallenge} from '../challenge/MCQChallenge.jsx'
import {useApi} from '../utils/api.js'

export function HistoryPanel() {
    const [history, setHistory] = useState([])
    const [isLoading, setIsLoading] = useState(true)
    const [error, setError] = useState(null)
    const {makeRequest}=useApi()
    const [classify, setClassify]= useState("all")
    useEffect(() => {
        fetchHistory()
    }, [])

    const fetchHistory = async () => {
        setIsLoading(false)
        setError(null)
        try{ 
            const data = await makeRequest("my-history")
            setHistory(data)
        }catch (err){
            console.log(err)
        }
        
    }

    if (isLoading) {
        return <div className="loading">Loading...</div>
    }
    if (error) {
        return <div className="error-message">
            <p>Error fetching history: {error.message}</p>
            <button onClick={fetchHistory}>Retry</button>
        </div>
    }


    return <div className='history-panel'>
        <h2>History</h2>
         <div className="difficulty-selector">
            <label htmlFor="difficulty">Search Challenges History By Difficulty</label>
            <select 
                id="classify_difficulty" 
                value={classify} 
                onChange={(e) => setDifficulty(e.target.value)}
            >
                <option value="all">All</option>
                <option value="easy">Easy</option>
                <option value="medium">Medium</option>
                <option value="hard">Hard</option>
            </select>
        </div>
        {history.length === 0 ? <p>No challenges history</p> : 
        <div>
            {history.map((challenge) => {
                return <MCQChallenge 
                challenge={challenge} 
                key={challenge.id} 
                showExplanation="true"
            />
            })}
        </div>
        }
    </div>
}
