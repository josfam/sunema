import { useForm } from 'react-hook-form';
import '../styles/auth.css'
import {UserService} from "../services/user-service.js";
import {useNavigate} from "react-router-dom";

/**
 * FIX: The Login component should allow users to try again after a failed login submission
 */

const Login = () => {
    const { register, handleSubmit, formState: { errors }, setError, clearErrors, reset } = useForm();
    const navigate = useNavigate();

    const onSubmit = async (data) => {
        // authenticate user
        try {
            const response = await UserService.authenticateUser(data)
            if (response.message === 'logged in') {
                navigate('/');
            }
        } catch (error) {
            setError('auth_error', {
                type: 'manual',
                message: 'Invalid username or password'
            })
        }
    };
    return (
        <div className={'auth-wrapper'}>
            <h1 className={'welcome-text'}>Welcome</h1>
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
                <button type={'submit'}>Login</button>
            </form>
        </div>
    );
};

export default Login;
