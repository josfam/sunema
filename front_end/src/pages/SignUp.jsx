import { useForm } from 'react-hook-form';
import  userService  from '../services/user-service';
import '../styles/auth.css'
import {useNavigate} from "react-router-dom";


const SignUp = () => {
    const { register, handleSubmit, formState: { errors }, setError, clearErrors } = useForm();
    const navigate = useNavigate();

    const onSubmit = async (data) => {
        // register new user
        try {
            const response = await userService.registerUser(data);
            if (response.message === 'user created') {
                navigate('/');
            }
        } catch (error) {
            setError('auth_error', {
                type: 'manual',
                message: 'Username already exists'
            })
            window.setTimeout(() => clearErrors('auth_error'), 1000);
        }
    };
    return (
        <div className={'auth-wrapper'}>
            <h1 id={'welcome-text'}>Sign Up</h1>
            <form onSubmit={handleSubmit(onSubmit)}>
                {errors.auth_error && <p>{errors.auth_error.message}</p>}
                <input
                    {...register('username', {
                        required: 'Username is required',
                        minLength: {value: 3, message: "Username must be at least 3 characters"},
                        maxLength: {value: 32, message: "Username must be at most 32 characters"}
                    })}
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
