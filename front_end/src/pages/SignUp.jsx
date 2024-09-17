import { useForm } from 'react-hook-form';
import { UserService } from '../services/user-service';
import '../styles/auth.css'
import {useNavigate} from "react-router-dom";
import {useState} from "react";


const SignUp = () => {
    const { register, handleSubmit, formState: { errors }, setError } = useForm();
    // const { error, setError } = useState('');
    const navigate = useNavigate();

    const onSubmit = async (data) => {
        // register new user
        try {
            const response = await UserService.registerUser(data);
            if (response.message === 'user created') {
                navigate('/');
            }
        } catch (error) {
            setError('auth_error', {
                type: 'manual',
                message: 'Username already exists'
            })
        }
    };
    return (
        <div className={'auth-wrapper'}>
            <h1 id={'welcome-text'}>Sign Up</h1>
            <form onSubmit={handleSubmit(onSubmit)}>
                {errors.auth_error && <p>{errors.auth_error.message}</p>}
                <input
                    {...register('username', {required: 'Username is required'})}
                    placeholder={'Enter your Username'}
                />
                {errors.username && <p>{errors.username.message}</p>}
                <input
                    {...register('password', {required: 'Password is required'})}
                    placeholder={'Enter your password'}
                />
                {errors.password && <p>{errors.password.message}</p>}
                <button type={'submit'}>Sign Up</button>
            </form>
        </div>
    );
};

export default SignUp;
