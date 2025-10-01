// /public/script.js

document.addEventListener('DOMContentLoaded', () => {
    const tg = window.Telegram.WebApp;
    tg.ready();
    tg.expand();
    
    // Меняем тему приложения в зависимости от настроек Telegram
    document.body.style.backgroundColor = tg.themeParams.bg_color || '#ffffff';
    document.body.style.color = tg.themeParams.text_color || '#000000';

    const loadingEl = document.getElementById('loading');
    const profileEl = document.getElementById('profile');
    const productsEl = document.getElementById('products');

    async function loadInitialData() {
        try {
            // Здесь будет код для запроса данных с вашего API
            // Например, GET /api/profile
            
            // Имитация загрузки
            await new Promise(resolve => setTimeout(resolve, 500));
            
            if (tg.initDataUnsafe && tg.initDataUnsafe.user) {
                document.getElementById('user-id').textContent = tg.initDataUnsafe.user.id;
            }
            
            // Показываем контент после "загрузки"
            loadingEl.classList.add('hidden');
            profileEl.classList.remove('hidden');
            productsEl.classList.remove('hidden');

        } catch (error) {
            loadingEl.textContent = 'Ошибка загрузки. Попробуйте перезайти.';
            tg.showAlert('Не удалось загрузить данные. ' + error.message);
        }
    }

    loadInitialData();
});