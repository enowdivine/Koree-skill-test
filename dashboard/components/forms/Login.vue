<template>
    <b-form @submit="onSubmit" v-if="show">
        <b-form-group id="input-group-2" label="Your Name:" label-for="input-2">
            <b-form-input
                id="input-2"
                v-model="form.username"
                placeholder="Enter name"
                autocomplete
                required
            ></b-form-input>
        </b-form-group>

        <b-form-group>
            <label for="text-password">Password</label>
            <b-form-input
                type="password"
                v-model="form.password"
                id="text-password"
                placeholder="Enter password"
                required
                aria-describedby="password-help-block"
            ></b-form-input>
        </b-form-group>

        <b-button type="submit" variant="primary">Submit</b-button>
    </b-form>
</template>

<script>
export default {
    name: 'Login',
    data() {
        return {
            form: {
                username: '',
                password: '',
            },
            show: true,
        };
    },

    methods: {
        async onSubmit(event) {
            event.preventDefault();
            if (this.form.username && this.form.password) {
                const data = new FormData();
                data.append('username', this.form.username);
                data.append('password', this.form.password);
                // const data = {
                //     username: this.form.username,
                //     password: this.form.password,
                // };
                try {
                    console.log(typeof data);
                    const response = await this.$axios.post('/auth/register', data, {
                        headers: {
                            Accept: 'multipart/form-data',
                            'Content-Type': 'application/json',
                        },
                    });
                    console.log('my response', response);
                    if ((response.status = 200)) {
                        this.$toast.success('Successfully authenticated', { duration: 5000 });
                        this.$store.commit('LOGIN', response.data);
                        this.$router.push({ path: 'contacts' });
                    }
                } catch (error) {
                    this.$toast.error('Invalid Credentials', { duration: 5000 });
                    console.error(error);
                }
            } else {
                this.error = true;
            }
        },
    },
};
</script>
