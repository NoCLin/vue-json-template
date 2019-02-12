<template>
    <div>
        <json-tree :raw="formatJSON(info)"></json-tree>
    </div>
</template>

<script>
    export default {
        methods: {
            formatJSON: function (theJSON) {
                return JSON.stringify(theJSON, true, 2);
            }
        },
        data: () => ({
            info: undefined, // 信息注入点
        }),
        created() {
        }
    }

</script>

