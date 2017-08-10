import _ from 'underscore';

export default {
    data: function () {
        return {
          elements: [],
          __parent_: undefined,
          loading: false,
        }
    },
    methods: {
        getElements: function () {
            if ('loading' in this) {
                if (!this.loading) {
                  this.toggleLoading()
                }
            }
            let url = this.url || arguments[0];
            if (!url) {
                throw new Error('URL no provehida para hacer consula de elementos');
            }
            this.$http.get(url)
                .then(response => {
                    this.$emit('http403', false);
                    this.elements = [];
                    for (let object of response.body) {
                        object.selected = false;
                        this.elements.push(object);
                    }
                    this.toggleLoading()
                }, response => {
                    if (response.status == 403) {
                        this.$emit('http403', true);
                    }
                    this.showSnackBar(response.body.detail || 'Ha ocurrido un error inesperado.')
                    this.toggleLoading()
                });
        },
        __getParent__: function () {
            if (!this.__parent_) {  // singleton
                let parent = this.$parent;
                while (parent !== undefined) {
                    if (parent.$parent === undefined) {
                        break;
                    }
                    parent = parent.$parent;
                }
                this.__parent_ = parent;
            }
            return this.__parent_;
        },
        getParent: function () {
            return this.__getParent__().$options.methods;
        },
        showSnackBar: function (value) {
            this.$emit('mostrarsnackbar', value);
        },
        eventCreatedObject: function (value) {
            value.selected = false;
            let exists = this.elements.find(x => x.id == value.id);
            if (exists) {
                for (let attr in exists) {
                    this.elements[this.elements.indexOf(exists)][attr] = value[attr] || exists[attr];
                }
            } else {
                this.elements.push(value);
            }
            this.selected = value;
        },
        eventUpdatedForm: function (value) {
            this.selected = value;
        },
        toggleLoading: function () {
            if ('loading' in this) {
                this.loading = !this.loading;
            }
        }
    }
}
