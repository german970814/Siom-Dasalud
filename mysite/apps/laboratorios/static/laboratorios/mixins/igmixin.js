import _ from 'underscore';

export default {
    data: {
        elements: [],
        snackbar: false,
        snackbarText: ''
    },
    methods: {
        getElements: function () {
            let url = this.url || arguments[0];
            if (!url) {
                throw new Error('URL no provehida para hacer consula de elementos');
            }
            this.$http.get(url)
                .then(response => {
                    for (let object of response.body) {
                        object.selected = false;
                        this.elements.push(object);
                    }
                }, response => {
                    showSnackBar(response.body.detail || 'Ha ocurrido un error inesperado.')
                });
        },
        showSnackBar: function (value) {
            this.snackbarText = value;
            this.snackbar = true;
        },
        eventCreatedObject: function (value) {
            value.selected = false;
            this.elements.push(value);
            this.selected = value;
        },
        eventUpdatedForm: function (value) {
            this.selected = value;
        },
    }
}
