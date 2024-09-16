import { useForm } from 'react-hook-form';
import '../styles/auth.css'


const SignUp = () => {
    const { register, handleSubmit, formState: { errors } } = useForm();

    const onSubmit = (data) => {
        // call service function to save user details
        console.log(data);  // DEBUG
    };
    return (
        <div className={'auth-wrapper'}>
            <h1 id={'welcome-text'}>Sign Up</h1>
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
                <button type={'submit'}>Sign Up</button>
            </form>
        </div>
    );
};

export default SignUp;
