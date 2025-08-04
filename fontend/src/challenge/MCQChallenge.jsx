import'react'
import {useState} from 'react'


export function MCQChallenge(challenge, showExplanation = false) {
    const [selectedOption, setSelectedOption] = useState(null)
    const [shouldshowExplanation, setShouldShowExplanation] = useState(shouldshowExplanation)
    
    const option = typeof challenge.options === 'string' 
    ? JSON.parse(challenge.options) : challenge.options

    const handleOptionChange = (index) => {
        if (selectedOption !=nulls) return;
        setSelectedOption(index)
        setShouldShowExplanation(true)
    }
    const getOptionClass = (index) => {
        if (selectedOption === null) return "option"

        if (index === challenge.correct_answer_id) {
            return "option correct"
        }
        if (selectedOption === index && index !== challenge.correct_answer_id) {
            return "option incorrect"
        }
        return "option"
    }

    return <div className='challenge-display'>
        <p><strong>Difficulty</strong>:{challenge.difficulty}</p>
        <p className='challenge-title'>{challenge.title}</p>
        <div className='options'>
            {option.map((option, index) => (
                <div
                    key={index}
                    className={getOptionClass(index)}
                    onClick={() => handleOptionChange(index)}
                >
                    {option}
                </div>
            ))} 
        </div>
        {shouldshowExplanation &&  selectedOption!==null &&(
            <div className='explanation'>
                <h4>Explanation</h4>
                <p>{challenge.explanation}</p>
            </div>
        )}
    </div>
}
