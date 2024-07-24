#include "Def.h"
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdint.h>

#include  "SLArpaas_test11_lib.h"

#define BOARD_IP_ADDRESS "192.168.15.116"




int main(int argc, char* argv[])
{
	NI_HANDLE handle;
	int ret;
	uint32_t    val;


	R_Init();


	if(R_ConnectDevice(BOARD_IP_ADDRESS, 8888, &handle) != 0) { printf("Unable to connect to the board!\n"); return (-1); };
#ifndef CUSTOM_EXAMPLE		
	
	/* //REMOVE THIS COMMENT TO ENABLE THE EXAMPLE CODE

	uint32_t status_osc = 0;
	uint32_t data_osc[1024];
	uint32_t read_data_osc;
	uint32_t valid_data_osc;
	uint32_t position = 0;
	int32_t decimator = 0;
	int32_t pre_trigger = 100;
	int32_t software_trigger = 0;
	int32_t analog_trigger = 1;
	int32_t digital0_trigger = 0;
	int32_t digital1_trigger = 0;
	int32_t digital2_trigger = 0;
	int32_t digital3_trigger = 0;
	int32_t trigger_channel = 0;
	int32_t trigger_edge = 0;
	int32_t trigger_level = 1000;
	int32_t timeout_osc = 1000;
	int32_t size_osc = 1024;
	uint32_t read_analog[1024];
	uint32_t read_digital0[1024];
	uint32_t read_digital1[1024];
	uint32_t read_digital2[1024];
	uint32_t read_digital3[1024];
	int Osc_Events = 10;
	int e = 0;
	while (e<Osc_Events)
	{
		if (OSCILLOSCOPE_Oscilloscope_0_SET_PARAMETERS(decimator, pre_trigger, software_trigger, analog_trigger, digital0_trigger, digital1_trigger,
			digital2_trigger, digital3_trigger, trigger_channel, trigger_edge, trigger_level, &handle) != 0) printf("Set Parameters Error");
		if (OSCILLOSCOPE_Oscilloscope_0_START(&handle) != 0) printf("Start Error");
		while (status_osc != 1)
			if (OSCILLOSCOPE_Oscilloscope_0_STATUS(&status_osc, &handle) != 0) printf("Status Error");

		if (OSCILLOSCOPE_Oscilloscope_0_POSITION(&position, &handle) != 0) printf("Position Error");
		if (OSCILLOSCOPE_Oscilloscope_0_DOWNLOAD(data_osc, size_osc, timeout_osc, &handle, &read_data_osc, &valid_data_osc) != 0) printf("Get Data Error");
		if (OSCILLOSCOPE_Oscilloscope_0_RECONSTRUCT(data_osc, position, pre_trigger, read_analog, read_digital0, read_digital1, read_digital2, read_digital3) != 0) printf("Reconstruction Error");
		e++;
	}
	printf("Download Finished");
*/
/* //REMOVE THIS COMMENT TO ENABLE THE EXAMPLE CODE

	uint32_t status_list = 0;
	uint32_t data_list[10];
	uint32_t read_data_list;
	uint32_t valid_data_list;
	uint32_t size_list = 10;
	int32_t timeout_list = 1000;
	uint32_t ReadListNumber = 0;
	uint32_t TargetDataNumber = 1000;
	uint32_t DownloadDataValues[1000];
	int i = 0;

	if (LISTMODULE_Digitizer_0_RESET(&handle) != 0) printf("Reset Error");
	if (LISTMODULE_Digitizer_0_START(&handle) != 0) printf("Start Error");
	if (LISTMODULE_Digitizer_0_STATUS(&status_list, &handle) != 0) printf("Status Error");
	if (status_list == 2)
	{
		while (ReadListNumber < TargetDataNumber) {
			if (LISTMODULE_Digitizer_0_DOWNLOAD(&data_list, size_list, timeout_list, &handle, &read_data_list, &valid_data_list) != 0) printf("Get Data Error");
			
			int k = 0;
			for (i = ReadListNumber; i < size_list; i++) {
				DownloadDataValues[i] = data_list[k];
				k++;
			}
			ReadListNumber = ReadListNumber+ size_list;
		}
		printf("Download Finished");
	}
*/


	
#else

#endif

	return 0;
}

 