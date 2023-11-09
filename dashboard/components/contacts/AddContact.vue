<template>
    <div>
        <b-button v-b-modal.modal-1 class="bg-primary ml-2 w-100">Add Contact</b-button>

        <b-modal id="modal-1" title="Add New Contact" @ok="onSubmit">
            <b-form @submit="onSubmit">
                <b-form-group id="input-group-1" label="Name:" label-for="input-1">
                    <b-form-input
                        id="input-1"
                        v-model="form.username"
                        placeholder="Enter username"
                        required
                    ></b-form-input>
                </b-form-group>

                <b-form-group id="input-group-1" label="Gender:" label-for="input-1">
                    <b-form-input id="input-1" v-model="form.gender" placeholder="Enter gender" required></b-form-input>
                </b-form-group>

                <b-form-group id="input-group-1" label="Address:" label-for="input-1">
                    <b-form-input
                        id="input-1"
                        v-model="form.address"
                        placeholder="Enter address"
                        required
                    ></b-form-input>
                </b-form-group>

                <b-form-group id="input-group-4" label="Phone number:" label-for="input-4">
                    <b-form-input
                        type="number"
                        id="input-4"
                        v-model="form.phone_number"
                        placeholder="Enter phone number"
                        required
                    ></b-form-input>
                </b-form-group>
                <b-form-group id="input-group-4" label="Email:" label-for="input-4">
                    <b-form-input id="input-4" v-model="form.email" placeholder="Enter email" required></b-form-input>
                </b-form-group>
            </b-form>
        </b-modal>
    </div>
</template>

<script>
export default {
    name: 'AddContact',
    data() {
        return {
            form: {
                username: '',
                gender: '',
                address: '',
                phone_number: '',
                email: '',
            },
        };
    },
    mounted() {},
    methods: {
        // Add new contact to database function
        async onSubmit(event) {
            event.preventDefault();
            if (this.form.username && this.form.gender) {
                try {
                    const data = {
                        username: this.form.username,
                        gender: this.form.gender,
                        address: this.form.address,
                        phoneNumber: this.form.phone_number,
                        email: this.form.email,
                    };
                    const token = localStorage.getItem('access_token');
                    if (token !== null) {
                        const response = await this.$axios.post('/contacts', data, {
                            headers: {
                                Authorization: `Bearer ${token}`,
                                Accept: 'multipart/form-data',
                                'Content-Type': 'application/json',
                            },
                        });
                        if ((response.status = 200)) {
                            this.$toast.success('COntact added', { duration: 5000 });
                            (this.form.username = ''),
                                (this.form.gender = ''),
                                (this.form.address = ''),
                                (this.form.phone_number = ''),
                                (this.form.email = '');
                        } else {
                            this.$toast.error('Not Authorized', { duration: 5000 });
                            this.$router.push({ path: '/' });
                        }
                    } else {
                        this.$toast.error('Not Authorized', { duration: 5000 });
                        this.$router.push({ path: '/' });
                    }
                } catch (error) {
                    this.$toast.error('Check all fields', { duration: 5000 });
                    console.error(error);
                }
            } else {
                this.$toast.error('Check all fields', { duration: 5000 });
            }
        },
    },
};
</script>

<style></style>
