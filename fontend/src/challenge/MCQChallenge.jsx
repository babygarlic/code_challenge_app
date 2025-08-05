import'react'
import {useState} from 'react'


export function MCQChallenge({ challenge, showExplanation = false }) {
    const [selectedOption, setSelectedOption] = useState(null)
    const [shouldShowExplanation, setShouldShowExplanation] = useState(showExplanation)

    const options = typeof challenge.options === 'string' 
    ? JSON.parse(challenge.options) : challenge.options
    if (!challenge || !challenge.difficulty || !challenge.title || !Array.isArray(options)) {
        return <div>Lỗi: Dữ liệu câu hỏi không hợp lệ: {challenge.difficulty},{challenge.title},{challenge.options}</div>;
    }
    const handleOptionChange = (index) => {
        if (selectedOption !=null) return;
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
            {options.map((option, index) => (
                <div
                    className={getOptionClass(index)}
                    key={index}
                    onClick={() => handleOptionChange(index)}
                >
                    {option}
                </div>
            ))} 
        </div>
        {shouldShowExplanation && selectedOption !== null &&(
            <div className='explanation'>
                <h4>Explanation</h4>
                <p>{challenge.explanation}</p>
            </div>
        )}
    </div>
}
