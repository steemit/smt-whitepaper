
#pragma once

#include <steemit/app/plugin.hpp>

namespace steemit { namespace plugin { namespace smt_struct {

using namespace steemit::chain;
using namespace steemit::protocol;

namespace detail {
class smt_struct_plugin_impl;
}

class smt_struct_plugin : public steemit::app::plugin
{
   public:
      smt_struct_plugin( steemit::app::application* app );
      virtual ~smt_struct_plugin();

      virtual std::string plugin_name()const override;
      virtual void plugin_initialize( const boost::program_options::variables_map& options ) override;
      virtual void plugin_startup() override;
      virtual void plugin_shutdown() override;

   private:
      std::shared_ptr< detail::smt_struct_plugin_impl > my;
};

struct smt_generation_unit
{
   flat_map< account_name_type, uint16_t >        steem_unit;
   flat_map< account_name_type, uint16_t >        token_unit;
};

struct smt_cap_commitment
{
   share_type            lower_bound;
   share_type            upper_bound;
   digest_type           hash;
};

struct smt_capped_generation_policy
{
   smt_generation_unit pre_soft_cap_unit;
   smt_generation_unit post_soft_cap_unit;

   smt_cap_commitment  min_steem_units_commitment;
   smt_cap_commitment  hard_cap_steem_units_commitment;

   uint16_t            soft_cap_percent;

   uint32_t            min_unit_ratio;
   uint32_t            max_unit_ratio;

   extensions_type     extensions;
};

typedef static_variant< smt_capped_generation_policy > smt_generation_policy;

struct smt_setup_operation
{
   account_name_type       control_account;
   uint8_t                 decimal_places = 0;
   int64_t                 max_supply = STEEMIT_MAX_SHARE_SUPPLY;

   smt_generation_policy   initial_generation_policy;

   time_point_sec          generation_end_time;
   time_point_sec          launch_time;

   extensions_type         extensions;
};


} } }


/*FC_REFLECT(steemit::plugin::smt_struct::smt_generation_unit,
    (steem_unit)
    (token_unit)
)

FC_REFLECT(steemit::plugin::smt_struct::smt_cap_commitment,
    (lower_bound)
    (upper_bound)
    (hash)
)

FC_REFLECT(steemit::plugin::smt_struct::smt_capped_generation_policy,
    (pre_soft_cap_unit)
    (post_soft_cap_unit)
    (min_steem_units_commitment)
    (hard_cap_steem_units_commitment)
    (soft_cap_percent)
    (min_unit_ratio)
    (max_unit_ratio)
    (extensions)
)

FC_REFLECT(steemit::plugin::smt_struct::smt_setup_operation,
    (control_account)
    (decimal_places)
    (max_supply)
    (initial_generation_policy)
    (generation_end_time)
    (launch_time)
    (extensions)
)

FC_REFLECT(steemit::plugin::smt_struct::stats_info,
    (current_supply)
    (block_id)
    (user_accounts)
    (timestamp)
)
*/
