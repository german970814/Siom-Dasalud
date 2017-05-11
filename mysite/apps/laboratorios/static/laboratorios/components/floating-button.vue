<script>
import Vue from 'vue/dist/vue.js';

export default {
    name: 'floating-button',
    data: function () {
        return {
          animated: false,
        }
    },
    created: function () {
        // console.log(this.$slots.default);
    },
    computed: {
        classesMain: function () {
            return {
              animated: true,
              // fadeIn: this.animated,
              // fadeOut: !this.animated,
              'ig-floating-button-main': true,
            }
        },
        classesChildren: function () {
            return {
              animated: true,
              fadeInUp: this.animated,
              fadeOutDown: !this.animated,
              'ig-floating-button': true,
            }
        }
    },
    methods: {
        genButtons: function () {
            let children = [];
            let index = 1;
            let margin = 0;
            let base = 80;
            if (this.animated) {
                for (let node of this.$slots.child) {
                    if (node.tag) {
                        children.push(
                            this.$createElement('div',
                            {
                              'class': this.classesChildren,
                              style: {
                                'margin-bottom': (base + (margin * (index))).toString() + 'px'
                              }
                            }, [node])
                        );
                        margin += 45;
                    }
                }
            }
            return children;
        }
    },
    render: function () {
        return this.$createElement('div', {
            on: {
                mouseover: () => {
                    this.animated = true;
                },
                mouseleave: () => {
                    this.animated = false;
                }
            }
        }, [
            this.$createElement('div', {
              'class': this.classesMain,
            },
            [
              this.$slots.default,
            ]),
            this.$createElement('div', {class: {'ig-floating-button-container': this.animated}}, [
              ...this.genButtons()
            ])
        ])
    },
}
</script>

<style lang="css">
.ig-floating-button {
    position: fixed;
    bottom: 0;
    right: 0;
    margin-right: 22px;
    /*margin-bottom: 90px;*/
    transition-duration: 50ms !important;
    animation-duration: 500ms;
}

.ig-floating-button-main {
    position: fixed;
    bottom: 0;
    right: 0;
    margin: 15px;
    transition-duration: 500ms;
    z-index: 10;
}

.ig-floating-button-main:hover {
    transform: rotate(360deg);
    transition-duration: 500ms;
}

.ig-floating-button-container {
    position: fixed;
    background-color: transparent;
    /*background-color: #323213;*/
    padding: 40px;
    right: 0;
    top: 0;
    z-index: 0;
    height: 100%;
}

/*.ig-rotator {
    transform: rotate(360deg);
    transition-duration: 500ms;
}*/
</style>
