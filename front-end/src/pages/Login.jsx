import { useForm } from 'react-hook-form';
import '../styles/Login.css'

const Login = () => {
    const { register, handleSubmit, formState: { errors } } = useForm();

    const onSubmit = (data) => {
        // call service function to save user details into database
        console.log(data)  // DEBUG
    }
    return (
        <div className={'login-wrapper'}>
            <h1 id={'welcome-text'}>Welcome</h1>
            <form onSubmit={handleSubmit(onSubmit)}>
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
    )
}


export default Login

