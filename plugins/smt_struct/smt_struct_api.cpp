
#include <steemit/app/api_context.hpp>
#include <steemit/app/application.hpp>

#include <steemit/plugins/smt_struct/smt_struct_api.hpp>
#include <steemit/plugins/smt_struct/smt_struct_plugin.hpp>

namespace steemit { namespace plugin { namespace smt_struct {

namespace detail {

class smt_struct_api_impl
{
   public:
      smt_struct_api_impl( steemit::app::application& _app );

      std::shared_ptr< steemit::plugin::smt_struct::smt_struct_plugin > get_plugin();

      steemit::app::application& app;
};

smt_struct_api_impl::smt_struct_api_impl( steemit::app::application& _app ) : app( _app )
{}

std::shared_ptr< steemit::plugin::smt_struct::smt_struct_plugin > smt_struct_api_impl::get_plugin()
{
   return app.get_plugin< smt_struct_plugin >( "smt_struct" );
}

} // detail

smt_struct_api::smt_struct_api( const steemit::app::api_context& ctx )
{
   my = std::make_shared< detail::smt_struct_api_impl >(ctx.app);
}

void smt_struct_api::on_api_startup() { }

} } }
