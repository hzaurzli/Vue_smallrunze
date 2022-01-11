<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item">
        <md-card>
          <md-card-header data-background-color="green">
            <h4 class="title">Data table</h4>
            <p class="category">
              Handcrafted by us with <i class="fa fa-heart heart"></i>
            </p>
          </md-card-header>
          <md-card-content>
            <input ref="getValue" type="text"/>
            <button type="button" @click="searchEvent">搜索</button>
            <vxe-grid
                    border
                    resizable
                    height="530"
                    :loading="loading"
                    :seq-config="{startIndex: (tablePage.currentPage - 1) * tablePage.pageSize}"
                    :columns="tableColumn"
                    :data="tableData">
              <template #pager>
                <vxe-pager
                        :layouts="['Sizes', 'PrevJump', 'PrevPage', 'Number', 'NextPage', 'NextJump', 'FullJump', 'Total']"
                        :current-page.sync="tablePage.currentPage"
                        :page-size.sync="tablePage.pageSize"
                        :total="tablePage.total"
                        @page-change="handlePageChange">

                </vxe-pager>
              </template>
            </vxe-grid>
          </md-card-content>
        </md-card>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from "axios";

  export default {
          data () {
            return {
              loading: false,
              search:"s",
              dat:[],
              lens:1,
              tablePage: {
                total: 0,
                currentPage: 1,
                pageSize: 3
              },
              tableColumn: [
                { type: 'seq', width: 60 },
                { type: 'checkbox', width: 50 },
                { field: 'name', title: 'Name',sortable:'True'},
                { field: 'nickname', title: 'Nickname',type:'html'},
                { field: 'role', title: 'Role' },
                { field: 'address', title: 'Address', showOverflow: true }
              ],
              tableData: []
            }
          },

          created(){
            this.search = this.$route.query.id;
            // console.log(this.$route.query);
          },

          beforeMount(){
            this.getdata();
          },

          mounted () {
            this.findList()
          },

          // beforeUpdate(){
          //   this.search = this.$route.path;
          //   // console.log(this.$route.query);
          // },

          updated(){
            this.getdata();
          },

          methods: {
            findList () {
              this.loading = true;
              setTimeout(() => {
                this.loading = false;
                this.tablePage.total = this.lens;
                this.tableData = this.dat;
              }, 300)
            },

            getdata(){
              console.log(this.search);
              axios.get('http://127.0.0.1:5000/table/'+this.tablePage.currentPage+'/'+this.search).then(response => {
                this.lens = response.data.lens;
                this.dat = response.data.categories;
              }).catch(function (error) {
                console.log(error);
              })
            },

            searchEvent () {
              var aa = this.$refs.getValue.value;
              this.search = aa;
              // console.log(this.search);
              this.findList();
            },

            handlePageChange ({ currentPage, pageSize }) {
              this.tablePage.currentPage = currentPage;
              this.tablePage.pageSize = pageSize;
              this.findList();
            }
          }
        }
</script>
