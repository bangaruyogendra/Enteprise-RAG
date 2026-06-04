import { useState } from 'react';
import api from '../api/api';

const FileUpload = () => {
    const [question, setQuestion] = useState('');
    const [user_id, setUser_id] = useState('');
    const [role, setRole] = useState('');
    const [department, setDepartment] = useState('');
    const [response, setResponse] = useState<string | null>(null);

    const handleSubmit = async (
        e: React.FormEvent<HTMLFormElement>
    ) => {
        e.preventDefault();

        try {
            const res = await api.post('/query', {
                question,
                user_id,
                role,
                department,
            });

            setResponse(res.data.answer);
        } catch (error) {
            console.error('Error submitting query:', error);
        }
    };

    return (
        <>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Question"
                    value={question}
                    onChange={(e) => setQuestion(e.target.value)}
                />
                <input
                    type="text"
                    placeholder="User ID"
                    value={user_id}
                    onChange={(e) => setUser_id(e.target.value)}
                />
                <input
                    type="text"
                    placeholder="Role"
                    value={role}
                    onChange={(e) => setRole(e.target.value)}
                />
                <input
                    type="text"
                    placeholder="Department"
                    value={department}
                    onChange={(e) => setDepartment(e.target.value)}
                />
                <button type="submit">Submit</button>
            </form>

            {response && <div>Response: {response}</div>}
        </>
    );
};

export default FileUpload;