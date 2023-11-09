export const state = () => ({
    user: {},
});

// USER MUTATIONS
export const mutations = {
    LOGIN: (state: { user: any }, data: any) => {
        state.user = data;
        localStorage.setItem('access_token', data.token);
    },
    LOGOUT: (state: { user: Object }) => {
        state.user = {};
        localStorage.removeItem('access_token');
    },
};
