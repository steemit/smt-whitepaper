

#include <steemit/plugins/smt_struct/smt_struct_api.hpp>
#include <steemit/plugins/smt_struct/smt_struct_plugin.hpp>

#include <steemit/chain/global_property_object.hpp>
#include <steemit/chain/account_object.hpp>
#include <steemit/chain/comment_object.hpp>

#include <fc/io/json.hpp>

#include <string>

namespace steemit { namespace plugin { namespace smt_struct {

using namespace steemit::chain;
using namespace steemit::protocol;

namespace detail {

class smt_struct_plugin_impl
{
   public:
      smt_struct_plugin_impl( steemit::app::application& app );
      virtual ~smt_struct_plugin_impl();

      virtual std::string plugin_name()const;
      virtual void plugin_initialize( const boost::program_options::variables_map& options );
      virtual void plugin_startup();
      virtual void plugin_shutdown();
      void on_applied_block( const chain::signed_block& b );
      void on_pre_operation( const operation_notification& o);

      steemit::app::application& _app;
      boost::signals2::scoped_connection _applied_block_conn;
};

smt_struct_plugin_impl::smt_struct_plugin_impl( steemit::app::application& app )
  : _app(app) {}

smt_struct_plugin_impl::~smt_struct_plugin_impl() {}

std::string smt_struct_plugin_impl::plugin_name()const
{
   return "smt_struct";
}

void smt_struct_plugin_impl::plugin_initialize( const boost::program_options::variables_map& options )
{
    ilog("smt_struct init.");
    //_applied_block_conn = _app.chain_database()->applied_block.connect(
    //  [this](const chain::signed_block& b){ on_applied_block(b); });
    //_app.chain_database()->pre_apply_operation.connect(
    //  [this](const operation_notification& o){ on_pre_operation( o ); } );

    //std::cout << "TEST HERE!" << "\n";
    //smt_setup_operation op;
    //std::cout << fc::json::to_string(op) << "\n";

}

void smt_struct_plugin_impl::plugin_startup()
{
   _app.register_api_factory< smt_struct_api >( "smt_struct_api" );
}

void smt_struct_plugin_impl::plugin_shutdown()
{
}

}

smt_struct_plugin::smt_struct_plugin( steemit::app::application* app )
   : plugin(app)
{
   FC_ASSERT( app != nullptr );
   my = std::make_shared< detail::smt_struct_plugin_impl >( *app );
}

smt_struct_plugin::~smt_struct_plugin() {}

std::string smt_struct_plugin::plugin_name()const
{
   return my->plugin_name();
}

void smt_struct_plugin::plugin_initialize( const boost::program_options::variables_map& options )
{
   my->plugin_initialize( options );
}

void smt_struct_plugin::plugin_startup()
{
   my->plugin_startup();
}

void smt_struct_plugin::plugin_shutdown()
{
   my->plugin_shutdown();
}

} } }

STEEMIT_DEFINE_PLUGIN( smt_struct, steemit::plugin::smt_struct::smt_struct_plugin )
