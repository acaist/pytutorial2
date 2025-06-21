document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');
    const usernameError = document.getElementById('username-error');
    const passwordError = document.getElementById('password-error');
    const togglePassword = document.getElementById('togglePassword');

    // 密码可见性切换
    togglePassword.addEventListener('click', () => {
        const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordInput.setAttribute('type', type);
        togglePassword.classList.toggle('fa-eye-slash');
        togglePassword.classList.toggle('fa-eye');
    });

    // 表单提交验证
    loginForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        let isValid = true;

        // 清空错误提示
        usernameError.style.display = 'none';
        passwordError.style.display = 'none';

        // 验证用户名
        if (!usernameInput.value.trim()) {
            usernameError.textContent = '请输入用户名';
            usernameError.style.display = 'block';
            isValid = false;
        }

        // 验证密码
        if (!passwordInput.value) {
            passwordError.textContent = '请输入密码';
            passwordError.style.display = 'block';
            isValid = false;
        } else if (passwordInput.value.length < 6) {
            passwordError.textContent = '密码至少需要6位';
            passwordError.style.display = 'block';
            isValid = false;
        }

        if (!isValid) return;

        // 模拟提交到 Flask 后端（实际项目中替换为 fetch 或 axios）
        try {
            const formData = new FormData(loginForm);
            const response = await fetch('/login', {
                method: 'POST',
                body: formData
            });

            const result = await response.json();
            if (response.ok) {
                // 登录成功，跳转到仪表盘
                window.location.href = '/dashboard';
            } else {
                // 显示后端返回的错误信息
                alert(result.message || '登录失败，请检查用户名和密码！');
            }
        } catch (error) {
            alert('网络错误，请稍后重试！');
        }
    });
});