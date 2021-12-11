var app = new Vue({
    el: '#app',
    vuetify: new Vuetify(),
    data: {
        loading1: false,
        loading2: false,
        img_src: null
    },
    methods: {
        async get_img() {
            this.loading1 = true;

            // Pythonから画像データ(Base64文字列)を読み込む
            const img_base64 = await eel.get_img()();

            // 画面に表示
            this.img_src = 'data:image/png;base64,' + img_base64;

            this.loading1 = false;
        },
        async gray_scale() {
            this.loading2 = true;


            let img = this.img_src;
            img = img.replace('data:image/png;base64,', '');

            // Pythonでグレースケール変換
            const img_base64 = await eel.gray_scale(img)();

            // 画面に表示
            this.img_src = 'data:image/png;base64,' + img_base64;

            this.loading2 = false;
        }
    }
});
