package com.kumar.practice;

import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;

public class CustomThreadPoolExecutor{
	/*
	Task is rejected...java.util.concurrent.FutureTask@35f983a6[Not completed, task = java.util.concurrent.Executors$RunnableAdapter@6442b0a6[Wrapped task = com.kumar.practice.CustomThreadPoolExecutor$$Lambda$23/0x00000008000c0640@60f82f98]]
	Task processed by Thread-3
	Task processed by Thread-1
	Task processed by Thread-0
	Task processed by Thread-2
	Task processed by Thread-1
	Task processed by Thread-0
	
	7th task is not accepted since max thread is 4 and queue size is 2. Hence its getting rejected using custom rejected Exception handler
	
	*/
	public static void main(String ars[]) {

		/*
		Generally ThreadPool min and max size are depends on various factors like the following
		- CPU cores
		- JVM Memory
		- Task Nature
		- Concurrency Requirement (high/medium/low)
		- Memory required to process a request
		- throughput etc
		
		To find minimum pool size
		No of thread = No of CPU core * ( 1+ request waiting time/ processing time)
		
		If its CPU intensive task, request waiting time is less and processing time is more
		If its I/O intensive task, processing time is more and request waiting time is less
	
		This is just a rough estimation which should still obey the JVM's memory allocation
		
		*/
		
		ThreadPoolExecutor threadPoolExecutor = new ThreadPoolExecutor(
				2,
				4,
				10,
				TimeUnit.MINUTES,
				new ArrayBlockingQueue<>(2),
				new CustomThreadFactory(),
				new CustomRejectedExecutionHandler());
		
		threadPoolExecutor.allowCoreThreadTimeOut(true);
		
		for (int index = 0; index < 7; index++) {
			
			threadPoolExecutor.submit(()->{
				try {
					Thread.sleep(2000);
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
				
				System.out.println("Task processed by " + Thread.currentThread().getName());
			});
		}
	}
}