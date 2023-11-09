<template>
    <div class="container border rounded mt-4 p-4 overflow-auto">
        <div>
            <h4>All Contacts</h4>
        </div>
        <div class="d-flex justify-content-center mb-3">
            <b-form-input v-model="filter" type="search" placeholder="Type to filter contacts"></b-form-input>
            <!-- Add Contact Modal Component -->
            <div class="w-25"><AddContact /></div>
        </div>

        <!-- Contact Table -->
        <b-table
            id="my-table"
            striped
            :filter="filter"
            @filtered="onFiltered"
            :fields="fields"
            :items="contacts"
            :per-page="perPage"
            :current-page="currentPage"
            medium
            class="mt-4"
            ><template v-slot:cell(actions)="{ item }">
                <span><b-button v-b-modal.modal-2 class="bg-success" @click="updateModal(item)">Edit</b-button></span>
                <span><b-btn @click="deleteContact(item)" class="bg-danger">Delete</b-btn></span>
            </template></b-table
        >

        <!-- Table Pagination -->
        <b-pagination
            v-model="currentPage"
            :total-rows="rows"
            :per-page="perPage"
            aria-controls="my-table"
        ></b-pagination>

        <!-- Edit COntact Modal -->
        <div>
            <b-modal id="modal-2" title="Edit Contact" @ok="updateContact">
                <b-form @submit="updateContact">
                    <b-form-group id="input-group-1" label="Contact Name:" label-for="input-1">
                        <b-form-input
                            id="input-1"
                            v-model="form.username"
                            placeholder="Enter username"
                            required
                        ></b-form-input>
                    </b-form-group>

                    <b-form-group id="input-group-3" label="Author Name:" label-for="input-3">
                        <b-form-select v-model="form.author">
                            <option v-for="item in authors" :key="item.id" v-bind:value="{ item }">
                                {{ item.author_name }}
                            </option>
                        </b-form-select>
                    </b-form-group>

                    <b-form-group id="input-group-3" label="Number of pages:" label-for="input-3">
                        <b-form-input
                            type="number"
                            id="input-3"
                            v-model="form.number_of_pages"
                            placeholder="Enter number of pages"
                            required
                        ></b-form-input>
                    </b-form-group>
                </b-form>
            </b-modal>
        </div>
    </div>
</template>

<script>
import AddContact from './AddContact.vue';

export default {
    components: {
        AddContact,
    },
    data() {
        return {
            // Table Data
            perPage: 6,
            currentPage: 1,
            rows: 1,
            fields: ['id', 'username', 'gender', 'address', 'phone_number', 'email', 'actions'],
            contacts: [],
            filter: null,
            output: null,

            // Form Data
            form: {
                id: '',
                username: '',
                gender: '',
                address: '',
                phone_number: '',
                email: '',
            },
        };
    },
    mounted() {
        this.getContacts();
    },
    methods: {
        onFiltered(filteredItems) {
            this.rows = filteredItems.length;
            this.currentPage = 1;
        },

        // Function to get contacts from database
        async getContacts() {
            try {
                const token = localStorage.getItem('access_token');
                if (token !== null) {
                    const response = await this.$axios.get('/contacts', {
                        headers: { Authorization: `Bearer ${token}` },
                    });
                    this.contacts = response.data;
                    this.rows = response.data.length;
                } else {
                    this.$toast.error('Not Authorized', { duration: 5000 });
                    this.$router.push({ path: '/' });
                }
            } catch (error) {
                console.error(error);
            }
        },

        // Function to set initial variables for a contact during update
        async updateModal(contact) {
            this.form.id = contact.id;
            this.form.username = contact.username;
            this.form.gender = contact.gender;
            this.form.address = contact.address;
            this.form.phone_number = contact.phoneNumber;
            this.form.email = contact.email;
        },

        // Function to update single contact
        async updateContact() {
            try {
                const data = {
                    id: this.form.id,
                    username: this.form.username,
                    gender: this.form.gender,
                    address: this.form.address,
                    phoneNumber: this.form.phone_number,
                    email: this.form.email,
                };
                if (data.id) {
                    const token = localStorage.getItem('access_token');
                    if (token !== null) {
                        const response = await this.$axios.put(`/contacts/${data.id}`, data, {
                            headers: {
                                Authorization: `Bearer ${token}`,
                                Accept: 'multipart/form-data',
                                'Content-Type': 'application/json',
                            },
                        });
                        if ((response.status = 200)) {
                            this.$toast.success('Contact updated', { duration: 5000 });
                            this.form.id = '';
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
                } else {
                    this.$toast.error('Check all fields', { duration: 5000 });
                }
            } catch (error) {
                this.$toast.error('An error occured', { duration: 5000 });
                console.error(error);
            }
        },

        // // Funtion to delete contact
        async deleteContact(contact) {
            if (confirm('Are you sure to delete contact?') === true) {
                const data = {
                    id: contact.id,
                };
                try {
                    const token = localStorage.getItem('access_token');
                    if (token !== null) {
                        const response = await this.$axios.delete(`/contacts/${data.id}`, {
                            headers: {
                                Authorization: `Bearer ${token}`,
                                Accept: 'multipart/form-data',
                                'Content-Type': 'application/json',
                            },
                            data,
                        });
                        if ((response.status = 200)) {
                            this.$toast.success('Contact deleted', { duration: 5000 });
                            return true;
                        } else {
                            this.$toast.error('Not Authorized', { duration: 5000 });
                            this.$router.push({ path: '/' });
                        }
                    } else {
                        this.$toast.error('Not Authorized', { duration: 5000 });
                        this.$router.push({ path: '/' });
                    }
                } catch (error) {
                    this.$toast.error('An error occured', { duration: 5000 });
                    console.error(error);
                }
            }
        },
    },
};
</script>
