
#pragma once

#include <fc/api.hpp>

namespace steemit { namespace app {
   struct api_context;
} }

namespace steemit { namespace plugin { namespace smt_struct {

namespace detail {
class smt_struct_api_impl;
}

class smt_struct_api
{
   public:
      smt_struct_api( const steemit::app::api_context& ctx );

      void on_api_startup();

      // TODO:  Add API methods here

   private:
      std::shared_ptr< detail::smt_struct_api_impl > my;
};

} } }

FC_API( steemit::plugin::smt_struct::smt_struct_api,
   // TODO:  Add method bubble list here
   )
