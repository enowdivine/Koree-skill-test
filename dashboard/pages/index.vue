<template>
    <div class="container w-25 mt-5 border p-3 rounded">
        <h3 class="fw-bold text-center">Login</h3>
        <Login />
    </div>
</template>

<script>
import Login from '../components/forms/Login.vue';
export default {
    components: {
        Login,
    },
};
</script>
